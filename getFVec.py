import cv2
import numpy as np

def clrHist(img):
	bins = 4;
	hist= cv2.calcHist([img],[0],None,[bins],[0,256]);
	hist = hist/sum(hist);
	return  hist;