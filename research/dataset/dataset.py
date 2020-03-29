import glob
import shutil
import os

for file in glob.glob("./icon/*.png"):
    file_path = (file.replace("_minimap_icon","").replace("\\","/"))
    file_name = file_path[7:-4]
    os.mkdir("./dataset/icon/"+file_name)
    shutil.copy(file, "./dataset/icon/"+file_name+"/"+file_name+".png")
    
    
    
    

for file in glob.glob("./hero/*.png"):
    file_path = (file.replace("_icon","").replace("\\","/"))
    file_name = file_path[7:-4]
    os.mkdir("./crop/"+file_name)
#    shutil.copy(file, "./dataset/hero/"+file_name+"/"+file_name+".png")
    
    
    
    

