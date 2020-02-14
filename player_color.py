import os
import numpy as np
for root, dirs, files in os.walk("./dataset/screen_header/"):
    print(files)
    
from PIL import  Image

def split(img):
    w,h = img.size
    r = []
    for i in range(5):
        r.append(img.crop((i*w/5+20,6,(i+1)*w/5-21,7)))
    return r

folder = "./dataset/screen_header/"
img = Image.open(folder+files[0])
w,h = 1366,768
header = None

if w*9 > h*21:
    delta_w = (w - w*0.75)
    header = img.crop(((w*0.335),0,(w-w*0.335),h-h*0.96))
    print(1)
else:
    delta_w = 0.556

    left = img.crop((w*0.28,1,w-w*delta_w,2))
    left = left.resize((210,18))

    right = img.crop((w*delta_w,1,w-w*0.28,2))
    right = right.resize((210,18))
    
    radiant = split(left)
    dire = split(right)
    
    player_color = []
    [player_color.append(np.array(i)[0][0])  for i in radiant]
    [player_color.append(np.array(i)[0][0]) for i in dire]

            
        
    