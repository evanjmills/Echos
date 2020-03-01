import cv2
import colorsys
import numpy as np
import pandas as pd

### get the images and scale them by 1/10 to get the of a 10x10 area ###
ImgL = cv2.imread('image_1.png')
resizeImgL = cv2.resize(ImgL, (0,0), fx=0.1, fy=0.1)
ImgR = cv2.imread('image_2.png')
resizeImgR = cv2.resize(ImgR, (0,0), fx=0.1, fy=0.1)
ImgS = cv2.imread('disparity_map.png',0)
resizeImgS = cv2.resize(ImgS, (0,0), fx=0.1, fy=0.1)

def hue2rgb(hue, value):
	return colorsys.hsv_to_rgb(hue, 1., value)


file = open('test.csv', 'w')

file.write(',x,y,z,r,g,b\n')

i = 1
for y in xrange(0, resizeImgS.shape[0]):
	for x in xrange(0, resizeImgS.shape[1]):
		b = (resizeImgL[y,x,0])/255.0
		g = (resizeImgL[y,x,1])/255.0
		r = (resizeImgL[y,x,2])/255.0
		z = resizeImgS[y,x]

		file.write(str(i) + "," + str(x*10) + "," + str(y*10) + "," + str(z*10) + "," + str((r)) + "," + str((g)) + "," + str((b)) + '\n')

		i+=1
file.close()
