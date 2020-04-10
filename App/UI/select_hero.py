import win32api, win32con, win32gui
from cefpython3 import cefpython as cef
import sys

URL = "file:///C:/Users/baltschun/Desktop/project/Portfolio-Template-Bootstrap-master/index.html"

class MyWindow:

    def __init__(self):
        win32gui.InitCommonControls()
        self.hinst = win32api.GetModuleHandle(None)
        className = 'MyWndClass'
        message_map = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        wc = win32gui.WNDCLASS()
        wc.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wc.lpfnWndProc = message_map
        wc.lpszClassName = className
        win32gui.RegisterClass(wc)
        style = win32con.WS_POPUP
        self.hwnd = win32gui.CreateWindow(
            className,
            '',
            style,
            win32con.CW_USEDEFAULT,
            win32con.CW_USEDEFAULT,
            2560,
            1080,
            0,
            0,
            self.hinst,
            None
        )
        win32gui.UpdateWindow(self.hwnd)
        win32gui.ShowWindow(self.hwnd, win32con.SW_MAXIMIZE)
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE, win32con.WS_EX_LAYERED)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST,0,0,2560,1080,0)
        win32gui.SetLayeredWindowAttributes(self.hwnd, win32api.RGB(255,255,255), 0, win32con.LWA_COLORKEY)
        
        sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
        cef.Initialize()
        
        window_info = cef.WindowInfo()
        window_info.SetAsChild(self.hwnd)
        window_info.SetTransparentPainting(True)
        
        settings = {
            "background_color":  0x00, #0xff000fff,
        }
        browser = cef.CreateBrowserSync(window_info, settings=settings, url=URL)

        browser.SendFocusEvent(True)
        browser.WasResized()
        
        cef.MessageLoop()
        cef.Shutdown()
        
    def OnDestroy(self, hwnd, message, wparam, lparam):
        win32gui.PostQuitMessage(0)
        return True

w = MyWindow()
win32gui.PumpMessages() 
