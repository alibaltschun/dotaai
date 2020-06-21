import win32api
import win32con
import win32gui
from cefpython3 import cefpython as cef
import sys
import os
import time

BASE = (os.path.dirname(os.path.realpath(__file__)))

with open(BASE + "/url.txt", "r") as file:
    URL = file.read()

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
        win32gui.SetWindowLong(self.hwnd, win32con.GWL_EXSTYLE,
                               win32con.WS_EX_LAYERED)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOPMOST,
                              0, 0, 2560, 1080, 0)
        win32gui.SetLayeredWindowAttributes(
                    self.hwnd, win32api.RGB(255, 255, 255), 0,
                    win32con.LWA_COLORKEY)

        sys.excepthook = cef.ExceptHook
        cef.Initialize()

        window_info = cef.WindowInfo()
        window_info.SetAsChild(self.hwnd)
        window_info.SetTransparentPainting(True)

        settings = {
            "web_security_disabled": True
        }
        browser = cef.CreateBrowserSync(
                    window_info, settings=settings, url=URL)

        browser.SendFocusEvent(True)
        browser.WasResized()

        cef.MessageLoop()
        cef.Shutdown()

    def OnDestroy(self, hwnd, message, wparam, lparam):
        win32gui.PostQuitMessage(0)
        return True


def plot():
    _ = MyWindow()
    win32gui.PumpMessages()


if __name__ == '__main__':
    plot()
    input("Press something to exit")
