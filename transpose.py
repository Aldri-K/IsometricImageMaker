import subprocess
import time
import pyautogui
import os
from PIL import Image
from PIL import Image, ImageOps
import shutil

def picClick(picNum):
    
    picPath = pyAutoPics +'\\' + str(picNum) + '.png'
    clickLocation = pyautogui.locateOnScreen(picPath, confidence = .9)
    clickPoint = pyautogui.center(clickLocation)
    pyautogui.click(clickPoint[0],clickPoint[1])
    time.sleep(0.5)

def picDouble(picNum): 
    picPath = pyAutoPics +'\\' + str(picNum) + '.png'
    clickLocation = pyautogui.locateOnScreen(picPath, confidence = .9)
    clickPoint = pyautogui.center(clickLocation)
    pyautogui.doubleClick(clickPoint[0],clickPoint[1])
    time.sleep(0.5)

def picCheck(picNum):
    print("picnum")
    time.sleep(0.2)
    try:
        picClick(27)
        picDouble(picNum)
        print(picNum + " not clicked")
    except:
        print("Already Clicked")

def startAuto():
    picClick(1)
    picClick(2)
    picClick(3)
    picClick(4)
    picClick(8)
    picClick(6)
    picClick(7)
    picClick(8)
    picClick(9)


def addProc():
    picDouble(10)
    picClick(11)
    picClick(20)
    picClick(12)


def shear():
    print("-------------------------------")
    print("shear")
    addProc()
    pyautogui.write('shear')
    picClick(24)
    picClick(25)
    picClick(28)
    picClick(29)
    pyautogui.press('backspace', presses=3)
    pyautogui.write('725')
    picDouble(21)
    picCheck(26)

def finalise():
    picClick(30)
    try:
        picClick(33)
        picClick(31)
    except:
        print("no overwrite required")
    time.sleep(30)
    os.system("TASKKILL /F /IM gimp-2.8.exe")
    # subprocess.Popen(r'explorer /select,"C:\Users\RDK\Downloads\Images\Transposition"')
    


def crop():
    pathForCrop = path = os.path.dirname(os.path.realpath(__file__)) +"\\Transposition\\"

    os.chdir(pathForCrop)
    srcFileNames = os.listdir()
    for img in srcFileNames:
        split_string = img.split(".", 1)
        name = split_string[0]
        im = Image.open(pathForCrop+img)
        # im.show()
        # Setting the points for cropped image
        left = 575
        top = 460
        right = 874
        bottom = 989
        im1 = im.crop((left, top, right, bottom))

        outpath = pathForCrop + name + "_wall" +".png"
        print("processed crop: "+ outpath)
        im1.save(outpath, 'PNG')
        shutil.move(outpath, os.path.dirname(os.path.realpath(__file__))+"\\Export\\" + name + "_wall" +".png")
        im_mirror = ImageOps.mirror(im1)
        outpath = pathForCrop + name + "_wall_flip"+".png"
        print("processed crop: "+ outpath)
        im_mirror.save(outpath, 'PNG')
        shutil.move(outpath, os.path.dirname(os.path.realpath(__file__))+"\\Export\\"+ name +  "_wall_flip"+".png")


def pilProcess():
    path = os.path.dirname(os.path.realpath(__file__)) 
    srcPath = path + "\\Textures"
    os.chdir(srcPath)
    srcFileNames = os.listdir()
    for img in srcFileNames:
        imgPath = srcPath + "\\" + img
        split_string = img.split(".", 1)
        name = split_string[0]

        image = Image.open(imgPath)
        old_size = image.size
        image = image.resize((166, 166))
        image = image.resize(old_size,Image.NEAREST)
        image = image.resize((300, 380))
        old_size = image.size
        new_size = (1450, 1450)
        new_im = Image.new("RGBA", new_size)   ## luckily, this is already black!
        new_im.paste(image, ((new_size[0]-old_size[0])//2,
                            (new_size[1]-old_size[1])//2))



        outpath = path + "\\Transposition\\" + name+".png"
        # new_im.show()
        print("processed: "+ outpath)
        new_im.save(outpath, 'PNG')



    

proc1 = subprocess.Popen('C:\\Program Files\\GIMP 2\\bin\\gimp-2.8.exe', shell=True)
pyAutoPics = os.path.dirname(os.path.realpath(__file__)) + "\\autoguiFiles"
time.sleep(10)
failCount = 0
def main():
    try:
        pilProcess()
        startAuto()
        shear()
        finalise()
        crop()

    except:
        global failCount
        failCount = failCount + 1
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("FAILED RUN")
        print("FAIL COUNT: " + str(failCount))
        os.system("TASKKILL /F /IM gimp-2.8.exe")
        if failCount < 5:
           subprocess.Popen('C:\\Program Files\\GIMP 2\\bin\\gimp-2.8.exe', shell=True) 
           time.sleep(10)
           main()
        elif failCount > 5:
            print("--------------------------------------------------------------------")
            print("WARNING APPLICATION HAS FAILED THE TRANSPOSITION STAGE TRY AGAIN")
            print("--------------------------------------------------------------------")
    
    print("--------------------------------------")
    print("IMAGE PROCESSING COMPLETE:")
    print("Files are located in the export folder")
    print("--------------------------------------")

main()
