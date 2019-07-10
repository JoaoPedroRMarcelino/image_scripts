import os
import csv
import json
import sys
import wget
from termcolor import colored
import requests


pathDataset   = 'dataset-exported.csv'
dirImageLabel = 'imageLabel'
dirMaskImage  = 'maskLabel'

prefixNameImage = 'fc_road_'
extPng = '.png'
extJpg = '.jpg'
zerosLeft = 5

if os.path.exists(dirImageLabel):
    os.rmdir(dirImageLabel)

if os.path.exists(dirMaskImage):
    os.rmdir(dirMaskImage)

os.makedirs(dirImageLabel)
os.makedirs(dirMaskImage)


with open(pathDataset) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    count_row = 0

    for row in csv_reader:
        if count_row == 0:
            print(colored(row,'green'))
        else:
            link_raw_image = row[2]
            link_mask_image =  json.loads(row[17])['Road']
            
            print(colored(f"Image: {prefixNameImage}{str(count_row).zfill(5)}{extPng}",'yellow'))
            
            imageName = f"{prefixNameImage}{str(count_row).zfill(5)}{extJpg}"

            pathSave = os.path.join(dirImageLabel, imageName)
            
            stream = requests.get(link_raw_image)
            with open(pathSave, 'wb') as f:
                f.write(stream.content)

            imageName = f"{prefixNameImage}{str(count_row).zfill(zerosLeft)}{extPng}"

            pathSave = os.path.join(dirMaskImage, imageName)
            
            stream = requests.get(link_mask_image)
            with open(pathSave, 'wb') as f:
                f.write(stream.content)

        count_row+=1

print(100*"*")
print("END")