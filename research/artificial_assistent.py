import os
import numpy as np
from PIL import ImageOps , ImageGrab 
from pygame import mixer
import pytesseract
from tkinter import Tk , Frame , Button
import boto3
import easygui

BASE =  os.path.abspath(os.path.dirname(__file__)).replace("\\","/")

running = True
root = None

def __play_mp3__(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def __teleport__(delta,w,h):   
    teleport = ImageGrab.grab(( delta[0],h*.97,delta[1],h*.985))
    
    avg_teleport = np.max(np.array(teleport))
    if avg_teleport < 100:
        __play_mp3__(BASE+"/static/teleport.mp3")
        
def __timer__(delta,w,h):    
    timer = ImageGrab.grab((delta,h*0.02,w-delta,h-h*0.965))
    timer = ImageOps.invert(timer)
    timer = pytesseract.image_to_string(timer,lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789:')
    return timer

def __check_user__():
    username = easygui.enterbox("insert your email address")
    
    ACCESS_KEY = "AKIAVSRG2BELW4TOFMP5"
    SECRET_KEY = "7Y+a4lBfgbnDkq1bAmEBwk8tYxLc39HQ65Qay+r9"
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
        return username, True
    else :
        return username, False
    
def start():
    """Enable scanning by setting the global flag to True."""
    global running
    running = True

def stop():
    """Stop scanning by setting the global flag to False."""
    global running
    running = False
    
def main():
    global root
    w,h = ImageGrab.grab().size
    delta_teleport = [ w*.635 if w*9 > h*21 else w*0.685,
                      w*.6455 if w*9 > h*21 else w*0.695]
    delta_timer = w*0.49 if w*9 > h*21 else w*0.484
    w,h, delta_teleport, 
    
    root = Tk()
    
    root.title("Title")
#    root.geometry("500x500")
    
    app = Frame(root)
    app.grid()
    
    b_start = Button(app, text="Start Scan", command=start)
    b_stop = Button(app, text="Stop", command=stop)
    
    b_start.grid()
    b_stop.grid()
    
    root.after(1000, scanning,w, h, delta_teleport, delta_timer,False ,2)  # After 1 second, call scanning
    root.mainloop()
    
def scanning(w, h, delta_teleport, delta_timer,start_asistent = False,last_minutes = 2):
#    print("AI assistent ready")
    
    if running:
        timer = __timer__(delta_timer,w,h)
        if ":" in timer:
            minutes , seconds = timer.split(":")
            if start_asistent:
                if minutes[-1:] == "4" or minutes[-1:] == "9":
                    if seconds == "40":
                        __play_mp3__(BASE+"/static/rune20.mp3")
                    elif seconds == "50":
                        __play_mp3__(BASE+"/static/rune10.mp3")
                if seconds == "45":
                    __play_mp3__(BASE+"/static/creep.mp3")
                
                elif seconds == "05" or seconds == "30":
                    __teleport__(delta_teleport,w,h)
                
                if int(minutes) < last_minutes:
                    start_asistent = False
            else :
                if int(minutes) > last_minutes:
#                        print("game started, AI assistent active")
                    start_asistent = True
                else:
                    last_minutes = int(minutes)
#        time.sleep(0.8)
        
    root.after(800,scanning,w, h, delta_teleport, delta_timer,start_asistent,last_minutes)
     
    
#if __name__ == "__main__":
#    username, exist = __check_user__()
#    if exist:
#        main()
#    else:
#        ctypes.windll.user32.MessageBoxW(0, "User {} is not registered".format(username), u"Error", 0)

        
        
        