import numpy as np
from matplotlib import pyplot as plt
from binarize import binarize
import cv2 as cv
from extractBlobs import extractBlobs
from findLBP import findLBP
from lbpHist import lbpHist
import pickle

fname='train_img.png'
trImg = cv.imread(fname, cv.IMREAD_GRAYSCALE);
ret, bwtrImg=cv.threshold(trImg, 122, 255, cv.THRESH_BINARY_INV)
bxs=extractBlobs(bwtrImg, False, True)
#bxs.sort()
# print(bxs)
samples = np.zeros((36, 69));
i=0
print(bxs[0])
for bx in bxs:
	# print(trImg.shape)
	cimg = trImg[bx[0]:bx[0]+bx[2],bx[1]:bx[1]+bx[3]];
	# print(cimg.shape)
	clbp = findLBP(cimg);
	chist = lbpHist(clbp);
	chist=chist.reshape((1, 69))
	# print(chist.shape);
	samples[i, :]=chist;
	i+=1
	# cv.imshow('img',cimg);
	# cv.waitKey(0)
resp=['9','8','7','6','5','4','3','2','1','0','Z','Y','X','W','V','U','T','S','R','Q','P','O','N','H','F','E','D','B','M','L','K','J','C','A','I','G']
responses=[ord(i) for i in resp]
# print(resp)
responses=np.asarray(responses)
responses=responses.reshape((36,1))
# print(responses)
print(responses.shape)
print(samples.shape)
with open('samples.data','wb') as f:
	pickle.dump(samples, f)
with open('responses.data','wb') as f:
	pickle.dump(responses, f)
print('samples and responses saved')
# print(samples)
#np.savetxt('samples.txt',samples)

# plt.imshow(trImg, cmap='gray')
# plt.show()
