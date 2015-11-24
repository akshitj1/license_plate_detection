import cv2
import numpy as np

def findLBP(img):
	m,n = img.shape
	lbp = np.zeros([m-2, n-2], np.uint8)
	for y in range(1, m-2):
		for x in range(1, n-2):
			ctr=mask=0
			for dx in range(-1, 2):
				for dy in range(-1, 2):
					if not(dx==0 and dy==0):
						mask |= (1 if img[y+dy,x+dx]<img[y,x] else 0)<<ctr
						ctr+=1
			lbp[y,x]=mask;
	return lbp