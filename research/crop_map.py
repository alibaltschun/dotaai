import os
from PIL import ImageOps, Image

folder = "./research/dataset/dataset/team/train_ori/dire/"
folder_output = "./research/dataset/dataset/team/train_crop/dire/"

for root, dirs, files in os.walk(folder):
    print(files)    


for file in files:
#    file = files[0] # 0 , 10, 96
    img = Image.open(folder+file)
#    img.show()
    
    _, h = img.size
    
    
    img = the_map = img.crop((0,h-h*0.225,h*0.225,h))
    
    img.save(folder_output+file)
#    img.show()