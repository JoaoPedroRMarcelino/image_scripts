## SIFT.py
- This code will calc the difference between the images and read all the images matrix one by one, the function findSimilarities will apply the sift method saving all images that dont repeat it self and discard the rest.

### Requirements
- Python 2.7
- pip install opencv-python==3.4.2.16
- pip install opencv-contrib-python==3.4.2.16
- pip install termcolor

### Optionals
- Change the variable **frame_start** to start the video in a specific frame.
- Change the variable **IMAGE_DIR** to point your video path.
- Change the variable **folderTosave** to point to folder that save the frames.
- Change the variable **thresholdDifference** to change the minimum threshold at compare two frames.

## differenceBetweenImages.py
- Calc the difference between two frames, and save the next frame that difference is less than a threshold

### Requirements
- Python 2.7
- pip install opencv-python==3.4.2.16
- pip install opencv-contrib-python==3.4.2.16
- pip install termcolor
### Optionals
- Change the variable **frame_start** to start the video in a specific frame.
- Change the variable **pathToVideo** to point your video path.
- Change the variable **folderToSave** to point to folder that save the frames.
- Change the variable **thresholdDifference** to change the minimum threshold at compare two frames.


## convertJpgToPng.py
- Convert images into a folder from jpg to png

### Requirements
- Python 3.5
- pip3.5 install --user Pillow==2.2.1
### Optionals
- Change the variable **mypath** to point folder that contains images in jpg format.
- Change the variable **destPath** to point folder that will saved the images in png format.


## getAllImages.py
- Get all images and mask from dataset generated by app.labelbox.com, and put a common name in both.

## Requirements
- Python 3.6
- pip3.6 install --user termcolor
- pip3.6 install python-csv
### Optionals
- Change the variable **pathDataset** to point the dataset path 
- Change the variable **dirImageLabel** to point folder that will saved the originals images.
- Change the variable **dirMaskImage** to point folder that will saved the mask images.
- Change the variable **prefixNameImage** to change the images name prefix
- Change the variable **zerosLeft** quantity of zeros of left in image name


## AdjustMask.py
- Adjust the image mask generate by app.labelbox.com, from transparent and white to red (road) and pink remaining

### Requirements
- Python 3.6
- pip3.5 install --user Pillow==5.2.1
### Optionals
- Change the variable **mypath** to point folder that contains the originals masks 
- Change the variable **destPath** to point folder that will saved the changed mask.
