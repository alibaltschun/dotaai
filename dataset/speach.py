import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[1].id) 


import glob
import shutil
import os

for file in glob.glob("./icon/*.png"):
    file_path = (file.replace("_minimap_icon","").replace("\\","/"))
    file_name = file_path[7:-4]
    engine.say(file_name.replace("_"," "))
    engine.runAndWait()