import cv2
from termcolor import colored
from os.path import join

#Value -1 start from begin 
frame_start = -1                        #CHANGE TO FRAME THAT THE VIDEO START
#Path to video to analysis
pathToVideo = join('..','10_min.mp4')   #CHANGE TO YOUR VIDEO PATH
#Folder to save the frames compared
folderToSave = 'toTrain'                #CHANGE TO SAVE IN FOLDER THAT YOU WANT
#Limit treshold to save next frame 
thresholdDifference = 150               #CHANGE TO YOUR ACCEPTABLE THRESHOLD

def main():
    print("Video Path: %s" % pathToVideo)

    cap = cv2.VideoCapture(pathToVideo)
    count = -1
    origin = 0
    frameOriginal = -1

    ############################
    #Frame Size
    yframeFrom = 220
    yframeTo = 720

    xFrameFrom = 0
    xFrameTo =  1280
    ############################

    ##BEGIN THE CAPTURE AT THE FRAME_START
    while count < frame_start:
        ret,frame = cap.read()
        count+=1    

    while cap.isOpened():
        ret,frame = cap.read()
        count+=1
        
        print("Frame: "+str(count))
        
        if count == frame_start+1:
            frameOriginal = frame[yframeFrom:yframeTo, xFrameFrom:xFrameTo]
            pathToSave = join(folderToSave, "%s.jpg" % (count))
            cv2.imwrite(pathToSave, frameOriginal)
        else:
            if not ret:
                break

            frameCompare = frame[yframeFrom:yframeTo, xFrameFrom:xFrameTo]
            
            #TO SEE THE FRAMES UNCOMMENT THE LINES BELOW
            # cv2.imshow("original", frameOriginal)
            # cv2.imshow('compare',frameCompare)
        
            difference = findSimilarities(frameOriginal,frameCompare)
            print("Dif: "+str(difference))
            print("Origin: "+str(origin))

            if(difference < thresholdDifference):
                print(colored("Capture",'green'))
                pathToSave = join(folderToSave, "%s.jpg" % (count))
                cv2.imwrite(pathToSave, frameCompare)
                frameOriginal = frameCompare.copy()
                origin = count
            else:
                print("Diff expected, less than %s" % str(thresholdDifference))
                print(colored("Pass",'red'))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            print("\n")

    cap.release()
    cv2.destroyAllWindows()

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
    # result = cv2.drawMatches(original, kp_1, compare, kp_2, good_points, None)
    # cv2.imshow("result", result)

    return lGoodPoints


if __name__ == '__main__':
    main()
        