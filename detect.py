import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from findLBP import findLBP
from lbpHist import lbpHist
from getFVec import clrHist
import pickle

tImg = cv.imread('image_0040.jpg',cv.IMREAD_GRAYSCALE);
img = cv.imread('cars_markus/image_0011.jpg',cv.IMREAD_GRAYSCALE);
img=cv.GaussianBlur(img, (3,3), 0)
tImg=cv.GaussianBlur(tImg, (3,3), 0)

tImg = cv.Sobel(tImg,cv.CV_8U,1,0,ksize=3)
img = cv.Sobel(img,cv.CV_8U,1,0,ksize=3)

imLbp = findLBP(img);
tLbp = findLBP(tImg);

h,w = imLbp.shape;

tHist=lbpHist(tLbp);
tcHist=clrHist(tImg);

minDist=100000

bBox=[0,0,0,0];
scaleStp=15;
moveStp=10;
ratio=(tImg.shape[1]*1.0)/tImg.shape[0]
bxs=[]
for scaleF in range(1,scaleStp/3):
	winW=int(scaleF*(w/scaleStp));
	winH=int(winW/ratio);
	print(scaleF);
	print(minDist)
	minDist=100000
	bBox=[0,0,0,0];
	for x in range(0,w-winW,moveStp):
		for y in range(0,h-winH,moveStp):
			cHist=lbpHist(imLbp[y:y+winH, x:x+winW]);
			ccHist=clrHist(img[y:y+winH, x:x+winW]);

			chDist = np.linalg.norm(cHist-tHist);
			ccDist = np.linalg.norm(ccHist-tcHist);
			wt=0.3
			cDist=(1-wt)*chDist + wt*ccDist

			# if(1.2*0.03>cDist):
			# 	print([cDist, y,x,winH,winW])
			if(minDist>cDist):
				minDist = cDist;
				bBox = [y,x,winH,winW];
	bxs.append((minDist, bBox))
	print(minDist, bBox);

bxs.sort()
print(bxs)

px=2
py=3
plt.subplot(py,px,1),plt.imshow(tImg,cmap = 'gray')
plt.subplot(py,px,2),plt.imshow(img,cmap = 'gray')
i=3
for i in range(0, 3):
	bx=bxs[i][1]
	imgD = img[bx[0]:bx[0]+bx[2],bx[1]:bx[1]+bx[3]];
	plt.subplot(py,px,i+3),plt.imshow(imgD,cmap = 'gray')

with open('bbox.txt', 'wb') as f:
	pickle.dump(bxs[0:3], f)
plt.show()
	