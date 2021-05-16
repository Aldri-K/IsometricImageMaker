import zipfile
import os
import glob
import time
import shutil 


path = os.path.dirname(os.path.realpath(__file__)) 
outPath = path + "\\Unpack"
srcPath = path + "\\zips"
finalPath = path + "\\Textures"
os.chdir(srcPath)
srcFileNames = os.listdir()

for zip in srcFileNames:
    zipPath = srcPath + "\\" + zip 
    with zipfile.ZipFile(zipPath, 'r') as zip_ref:
        zip_ref.extractall(outPath)

  
os.chdir(outPath)
srcFileNames = os.listdir()
for file in srcFileNames:
   if "Color" not in file:
       print("Not in " + file)
       os.remove(file)
   else:
       try:
            imgPath = os.getcwd() + "\\" + file
            shutil.move(imgPath, finalPath) 
       except:
            print("An exception occurred")
            
os.system('python ' + path + '\\im.py')
