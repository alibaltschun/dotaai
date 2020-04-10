
import os
for root, dirs, files in os.walk("./valid_ori/"):
    print(files)
    
from PIL import Image

def split(img):
    w,h = img.size
    r = []
    for i in range(5):
        r.append(img.crop((i*w/5,0,(i+1)*w/5,h)))
    return r

ii=0
folder = "./valid_ori/"

# only work for ultrawide
for file in files:
    img = Image.open(folder+file)
    w,h = img.size
    
    header = img.crop(((w*0.205),0,(w-w*0.205),h-h*0.93))
#    header.show()

    w,h = header.size
    left = header.crop((0,0,w*.413,h))
#    left.show()
        
    right = header.crop((w-w*.413,0,w,h))
#    right.show()
        
    radiant = split(left)
    dire = split(right)
        

#    [i.show() for i in radiant]
#    [i.show() for i in dire]
    
    for crop in radiant:
        crop.save("./valid_crop/"+str(ii)+".png")
        ii += 1
    for crop in dire:
        crop.save("./valid_crop/"+str(ii)+".png")
        ii += 1
            



    