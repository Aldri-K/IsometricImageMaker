from PIL import Image
import os
import PIL
import glob

path = os.path.dirname(os.path.realpath(__file__)) 
# os.chdir(path)
# print(os.listdir())




def tileMapGen(img):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    imgPath = dir_path + "\\Textures\\" + img
    
    split_string = img.split(".", 1)
    name = split_string[0]

    image = Image.open(imgPath)
    old_size = image.size
    image = image.resize((166, 166))
    image = image.resize(old_size,Image.NEAREST)
    new_size = (1450, 1450)
    new_im = Image.new("RGBA", new_size)   ## luckily, this is already black!
    new_im.paste(image, ((new_size[0]-old_size[0])//2,
                        (new_size[1]-old_size[1])//2))

    rotated = new_im.rotate(45)
    resized_image = rotated.resize((600,300))
    # resized_image.show()

    outpath = dir_path + "\\Export\\" + name+".png"
    resized_image.save(outpath, 'PNG')
    print("processed: " +name)


srcPath = path + "\\Textures"
os.chdir(srcPath)
srcFileNames = os.listdir()
for img in srcFileNames:
    tileMapGen(img)

os.system('python ' + path + '\\transpose.py')