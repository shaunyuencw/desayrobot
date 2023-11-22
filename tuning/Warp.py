import cv2
import numpy as np
import warp_utils as utils


def getLaneCurve(img):

    imgCopy = img.copy()

    #### STEP 1
    imgThres = utils.thresholding(img)

    #### STEP 2
    h, w, c = img.shape
    points = utils.valTrackbars()
    imgWarp = utils.warpImg(img, points, w, h)
    imgWarpPoints = utils.drawPoints(imgCopy, points)

    # cv2.imshow('Thres', imgThres)
    cv2.imshow('Warp', imgWarp)
    cv2.imshow('Warp Points', imgWarpPoints)
    

if __name__ == "__main__":
    cap = cv2.VideoCapture('vid1.mp4')
    intialTracbarVals = [102, 80, 20, 214]
    utils.initializeTrackbars(intialTracbarVals)
    frameCounter = 0
    while True:
        frameCounter += 1
        if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            frameCounter = 0

        success, img = cap.read()
        img = cv2.resize(img,(480,240))

        getLaneCurve(img)
        # cv2.imshow('Vid', img)
        cv2.waitKey(1)