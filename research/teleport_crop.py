import os
from PIL import ImageOps, Image

#folder = "./research/dataset/dataset/teleport/valid_ori/0/"
#folder_output = "./research/dataset/dataset/teleport/valid_crop/0/"

folder = "./research/dataset/screen/"
for root, dirs, files in os.walk(folder):
    print(files)    


for file in files:
    file = files[3] # 0 , 10, 96
    img = Image.open(folder+file)
#    img.show()
    
    screen_width, screen_height = img.size
    
    delta_teleport = []
    if screen_width*9 > screen_height*21:
        delta_teleport.append(screen_width*.625)
        delta_teleport.append(screen_width*.665)
    else:
        delta_teleport.append(screen_width*0.66)
        delta_teleport.append(screen_width*0.74)
    
    img = img.crop((
            int(delta_teleport[0]),
            int(screen_height*.93),
            int(delta_teleport[1]),
            int(screen_height)))
    
#    img.save(folder_output+file)
    img.show()

