import sys
import os
import numpy as np
from termcolor import colored
from PIL import Image, ImageDraw, PILLOW_VERSION
from os.path import isfile, join

mypath = 'maskLabel'
destPath = 'maskLabelAdjusted'

red = (255, 0, 0, 255)
pink = (255, 0, 255, 255)

white = (255, 255, 255, 255)
transparent = (0, 0, 0, 0)

if os.path.exists(destPath):
    os.rmdir(destPath)

os.makedirs(destPath)

onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    imgPath = os.path.join(mypath, f)
    print(colored(f,'yellow'))
    im = Image.open(imgPath)
    
    width, height = im.size
    count = 0
    for y in range(0,height):
        if count == 2:
            break

        for x in range(0,width):
            channels_xy = im.getpixel((x,y))
            if channels_xy == white:
                ImageDraw.floodfill(im, xy=(x,y), value=pink, thresh=0)
                count+=1
                break
            elif channels_xy == transparent:
                ImageDraw.floodfill(im, xy=(x,y), value=red, thresh=0)
                count+=1
                break

    pathToSave = os.path.join(destPath,f)
    im.save(pathToSave)

print(100*"*")
print("END")