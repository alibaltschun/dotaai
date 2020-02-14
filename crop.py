import os
for root, dirs, files in os.walk("./dataset/screen_header/"):
    print(files)
    
from PIL import ImageOps, Image

def split(img):
    w,h = img.size
    r = []
    for i in range(5):
        r.append(img.crop((i*w/5,0,(i+1)*w/5,h)))
    return r

ii=0
folder = "./dataset/screen_header/"
for file in files:
    img = Image.open(folder+file)
    
#    size = map(int,file.replace(".png","").split("x"))
#    w,h = size
    w,h = 1366,768
    header = None
    
    if w*9 > h*21:
        delta_w = (w - w*0.75)
        header = img.crop(((w*0.335),0,(w-w*0.335),h-h*0.96))
        print(1)
    else:
#        img = img.resize(size,Image.ANTIALIAS)
        delta_w = 0.556
#        header = img.crop((w*0.28,0,w-w*0.28,h-h*0.96))
        left = img.crop((w*0.28,4,w-w*delta_w,h-h*0.965-3))
        left = left.resize((210,18))
#        left.show()
        right = img.crop((w*delta_w,4,w-w*0.28,h-h*0.965-3))
        right = right.resize((210,18))
        
        radiant = split(left)
        dire = split(right)
        
#        right.show()
#        print(left.size)
#        print(right.size)
#        [i.show() for i in radiant]
#        [i.show() for i in dire]
        for crop in radiant:
            crop.save("./dataset/crop/"+str(ii)+".png")
            ii += 1
        for crop in dire:
            crop.save("./dataset/crop/"+str(ii)+".png")
            ii += 1
            
            
        
    