#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      RANJEET
#
# Created:     17-08-2022
# Copyright:   (c) RANJEET 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pyautogui
from PIL import Image, ImageGrab
import time
#from numpy import asarray

def hit(key):
    pyautogui.keyDown(key)

def takescreenshot():
    image = ImageGrab.grab().convert('L')
    #image.show()
    return image

def iscollide(data):
    for i in range(200,220):
        for j in range(480,490):
            if data [i, j] < 100:
                return True
    return False

if __name__=="__main__":
    time.sleep(2)
    hit("up")
    while True:
        image=takescreenshot()
        data = image.load()
        if iscollide(data):
            hit("up")
    #print(asarray(image))

        #image.show()
