import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def binarize(img, thresh, debug=False):
	ret, bImg=cv.threshold(img, 255*thresh, 255, cv.THRESH_BINARY)
	if debug:
		plt.subplot(1,2,1), plt.imshow(img, cmap='gray')
		plt.subplot(1,2,2), plt.imshow(bImg, cmap='gray')
		plt.show()
	return bImg