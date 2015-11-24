import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from binarize import binarize

#img=cv.imread('lp_full.jpg', cv.IMREAD_GRAYSCALE)
# cImg=cv.imread('lp_full.jpg')
def extractBlobs(img, doFilter=True, forOCR=False):
	#img=cv.cvtColor(cImg, cv.COLOR_BGR2GRAY)
	bImg=binarize(img, 0.5)
	if forOCR:
		mode=cv.RETR_EXTERNAL 
	else: 
		mode=cv.RETR_LIST
	contours,hierarchy = cv.findContours(bImg, mode, cv.CHAIN_APPROX_NONE)
	print(len(contours))
	H, W = bImg.shape
	area=H*W
	bxs=[]
	for cnt in contours:
		if((not doFilter) or (cv.contourArea(cnt)>area/100 and cv.contourArea(cnt)<area/20)):
			x,y,w,h = cv.boundingRect(cnt)
			bxs.append((y,x,h,w))
	return bxs