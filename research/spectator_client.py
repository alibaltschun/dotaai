import tkinter
from tkinter import Tk
import win32api, win32con, pywintypes
from PIL import ImageTk , Image
import urllib.request
import sys
import os
import boto3

STATIC = "./static/"

DELAY = 5

def __setup_label__(endpoint,file,position):
    print(endpoint+"/"+file)
    urllib.request.urlretrieve(endpoint+"/"+file, STATIC+file)
    img = ImageTk.PhotoImage(Image.open(STATIC+file))
    label = tkinter.Label(image = img)
    label.master.overrideredirect(True)
    label.master.geometry(position)
    label.master.lift()
    label.master.wm_attributes("-topmost", True)
    label.master.wm_attributes("-disabled", True)
    
    hWindow = pywintypes.HANDLE(int(label.master.frame(), 16))
    exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
    win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)
    
    return label

def __refresh_label__(label,endpoint,file):
    try:
        urllib.request.urlretrieve(endpoint+"/"+file, STATIC+file)
        img = ImageTk.PhotoImage(Image.open(STATIC+file))  
        label.config(image = img)
        label.image = img
    except:
        None
    label.after(1000,__refresh_label__,label,endpoint,file)


def __show_hide__(label):
    if label.winfo_viewable():
        label.withdraw() 
    else:
        label.deiconify()

def close(arr_root):
    for label in arr_root:
        label.destroy()
    sys.exit()
    

def get_url(username):
    ACCESS_KEY = "AKIAVSRG2BELW4TOFMP5"
    SECRET_KEY = "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"
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    
    dynamodb = session.resource('dynamodb', 
                              region_name='ap-southeast-1',)
    
    table = dynamodb.Table("dotaai_dev")
    
    res =  table.get_item(
        Key={'id':username})
    if 'Item' in res:
        return res['Item']['server_url']
    else :
        return None

def setup(username):
    if not os.path.exists(STATIC[1:]):
        os.makedirs(STATIC[1:])
        
    r = get_url(username)
    if r is not None:
        try:
            urllib.request.urlretrieve(r+"/map.jpg", STATIC+"map.jpg")
            return r
        except:
            return None
    return r
    
def main(r):

    root_map = Tk()
    
    label_map = __setup_label__(r,"map.jpg","+1+480")
    __refresh_label__(label_map,r,"map.jpg")
    
    label_map.pack(expand=True)
    
    root_setting = Tk()
    
    button_map_toggle = tkinter.Button(root_setting, text ="toggle Map", command = lambda:__show_hide__(root_map))
    button_close = tkinter.Button(root_setting, text ="close program", command = lambda:close([root_map,root_setting]))
    
    button_map_toggle.pack()
    button_close.pack()
    
    label_map.mainloop()
    
#if __name__ == "__main__":
#    r,username = setup()
#    if r is not False:
#        while True:
#            main(r)
#            time.sleep(DELAY)
#    else:
#        ctypes.windll.user32.MessageBoxW(0, "{} not exist".format(username), u"Error", 0)


