
import os
for root, dirs, files in os.walk("./train_ori/gameplay"):
    print(files)
    
from PIL import Image

ii=0
folder = "./train_ori/gameplay/"

# only work for ultrawide
for file in files:
    img = Image.open(folder+file)
    w,h = img.size
    
    left_top = img.crop((0,0,h*0.15,h*0.15))
    
    left_top.save("./train_crop/gameplay/"+str(ii)+".png")
    ii += 1



    