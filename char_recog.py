import pickle
import numpy as np
import cv2 as cv

def getModel():
	with open('samples.data','rb') as f:
		samples=pickle.load( f)
	with open('responses.data','rb') as f:
		responses=pickle.load( f)

	model=cv.KNearest()
	model.train(samples.astype(np.float32), responses)
	print('model created')

	return model;