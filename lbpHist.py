import cv2
import numpy as np

def lbpHist(lbp):
	bins = 69;
	Hist= cv2.calcHist([lbp],[0],None,[bins],[0,256]);
	Hist = Hist/sum(Hist);
	return  Hist;