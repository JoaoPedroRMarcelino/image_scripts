#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pip install opencv-python==3.4.2.16
#pip install opencv-contrib-python==3.4.2.16
#pip install termcolor


# In[1]:


from PIL import Image
import glob
import cv2
from termcolor import colored
from os.path import join


# In[3]:


IMAGE_DIR = join('zip10')
images = glob.glob(f'{IMAGE_DIR}/*.jpg')
folderTosave = "Tosave"
print(f'Found {len(images)} images')
thresholdDifference = 5
frame_start = -1


# In[5]:


def main():
    print("Image Path: %s" % IMAGE_DIR)
    for image in images:
        img = Image.open(f'{image}')
        width, height = img.size[:2]
        width, height = int(width), int(height)
    
    count = -1
    origin = 0
    frameOriginal = 0
    ############################
    #Frame Size
    yframeFrom = 0
    yframeTo = height

    xFrameFrom = 0
    xFrameTo =  width

    for img in glob.glob(f'{IMAGE_DIR}/*.jpg'):
        count+=1
        cap = cv2.imread(img)
        ret = cap
        print("Frame: "+str(count))
        if count == frame_start+1:
            frameOriginal = cap[yframeFrom:yframeTo, xFrameFrom:xFrameTo]
            pathToSave = join(folderTosave, "%s.jpg" % (count))
            cv2.imwrite(pathToSave, frameOriginal)
        else:
            if not ret.any():
                break
            frameCompare = cap[yframeFrom:yframeTo,xFrameFrom:xFrameTo]
            #if u wanna see what frames r being compared
            #uncommente the lines below
            #cv2.imshow("Original", frameOriginal)
            #cv2.imshow("Comparacao",frameCompare)
            #cv2.waitKey(0)
            #cv2.destroyAllWindows()
            try:
                difference = findSimilarities(frameOriginal,frameCompare)
                if(difference > thresholdDifference):
                    print(colored("Accepted",'green'))
                    pathToSave = join(folderTosave, "%s.jpg" % (count))
                    cv2.imwrite(pathToSave, frameCompare)
                    frameOriginal = frameCompare.copy()
                else:
                    print("Diff expected, less than %s" % str(thresholdDifference))
                    print(colored("Denied",'red'))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                print("\n")
            except:
                continue
        
def findSimilarities(original, compare): 
    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(original, None)
    kp_2, desc_2 = sift.detectAndCompute(compare, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_1, desc_2, k=2)

    good_points = []
    ratio = 0.6
    for m, n in matches:
        if m.distance < ratio*n.distance:
            good_points.append(m)
    lGoodPoints = len(good_points)

    #TO SEE THE FRAME COMPARED UNCOMMENT THE LINES BELOW
    #result = cv2.drawMatches(original, kp_1, compare, kp_2, good_points, None)
    #cv2.imshow("result", result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return lGoodPoints
if __name__ == '__main__':
    main()


# In[ ]:




