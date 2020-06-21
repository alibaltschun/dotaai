import os
import time
import win32api
import win32con
import win32gui
from cefpython3 import cefpython as cef

BASE = (os.path.dirname(os.path.realpath(__file__)))

with open(BASE + "/url.txt", "r") as file:
    URL = file.read()

print(URL)
time.sleep(100)
