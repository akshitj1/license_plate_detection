import pickle
import numpy as np
from matplotlib import pyplot as plt
from binarize import binarize
import cv2 as cv
from extractBlobs import extractBlobs
from findLBP import findLBP
from lbpHist import lbpHist
from char_recog import getModel
import pytesseract as ptess
import Image

with open('bbox.txt', 'rb') as f:
	bxs=pickle.load(f)
fname='cars_markus/image_0011.jpg'
# trImg = cv.imread('train_img.png',cv.IMREAD_GRAYSCALE)
cImg = cv.imread(fname)
img=cv.cvtColor(cImg, cv.COLOR_BGR2GRAY)

# bx = [226, 381, 75, 32]

# trImg = trImg[bx[0]:bx[0]+bx[2],bx[1]:bx[1]+bx[3]]
bx=bxs[0][1]
cimgD = cImg[:][bx[0]:bx[0]+bx[2],bx[1]:bx[1]+bx[3]] 
# print(bxs)
imgD = img[bx[0]:bx[0]+bx[2],bx[1]:bx[1]+bx[3]];
bimgD=binarize(imgD, 0.5)
bxs=extractBlobs(imgD)

model = getModel();

# clbp = findLBP(trImg);
# chist = lbpHist(clbp);
# chist = chist.reshape((1, 69)).astype(np.float32);
# retval, results, neigh_resp, dists = model.find_nearest(chist, k = 1)
# string = chr(int((results[0][0])))
# print(string)

i=0
for cbx in bxs:
	y,x,h,w=cbx
	print(cbx)
	cimg = imgD[cbx[0]:cbx[0]+cbx[2],cbx[1]:cbx[1]+cbx[3]]
	# plt.imshow(cimg, cmap='gray')
	# plt.show()
	cv.imwrite('test/'+str(i)+'.bmp', cimg)
	print(ptess.image_to_string(Image.open('test/'+str(i)+'.bmp') ,config='-psm 10'))
	i+=1
	# cv.imwrite('test/'+str(i)+'.jpg', cimg)
	# plt.imshow(cimg, cmap='gray')
	# plt.show()
	# break
	# clbp = findLBP(cimg);
	# chist = lbpHist(clbp);
	# chist = chist.reshape((1, 69)).astype(np.float32);
	# retval, results, neigh_resp, dists = model.find_nearest(chist, k = 1)
	# string = chr(int((results[0][0])))
	# print(string)
	cv.rectangle(cimgD,(x,y),(x+w,y+h),(0,255,0),2)
px=1
py=2
plt.subplot(py,px,1),plt.imshow(cimgD)
plt.subplot(py,px,2),plt.imshow(bimgD,cmap = 'gray')
plt.show()