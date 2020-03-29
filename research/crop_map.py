import os
import numpy as np
for root, dirs, files in os.walk("./dataset/screen_map/"):
    print(files)
    
from PIL import ImageOps, Image

w,h = 1366,768
folder = "./dataset/screen_map/"
for file in files:
    img = Image.open(folder+file)
    img.show()
    the_map = img.crop((0,h-h*0.26,h*0.26,h))
    the_map.show()
    w,h = the_map.size
    mid = the_map.crop((h*0.30,h*0.35,h*0.65,h*0.7))
    mid.show()
    
#    size = map(int,file.replace(".png","").split("x"))
#    w,h = size
    w,h = 1366,768
    
    player_color = [
            [67,56,233,255],
            [87,211,165,255], 
            [180,0,162,255],
            [210,207,8,255],
            [231,174,0,255],
            [255,97,185,255],
            [146,188,68,255],
            [60,197,228],
            [0,132,38,255],
            [164,104,0]
            ]
    
    mid_player = [0 for i in range(10)]
    
    pix = np.array(mid).tolist()
    for i in range(len(pix)):
        for j in range(len(pix)):
            for k in range(len(player_color)):
                if pix[i][j] == player_color[k]:
                    mid_player[k] = 1
        
    