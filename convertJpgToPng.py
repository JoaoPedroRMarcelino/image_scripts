import os
from PIL import Image
from os.path import isfile, join

mypath = 'imageLabel'
destPath = 'imageLabelPng'


if os.path.exists(destPath):
    os.rmdir(destPath)

os.makedirs(destPath)

onlyfiles = [f for f in os.listdir(mypath) if isfile(join(mypath, f))]

for f in onlyfiles:
    print(f)
    im = Image.open(os.path.join(mypath, f))
    imgPath = os.path.join(destPath, f.replace('jpg','png'))
    im.save(imgPath, "PNG")