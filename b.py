import numpy as np
import cv2
from matplotlib import pyplot as plt



imgL = cv2.imread('image_1.png',0)
imgR = cv2.imread('image_2.png',0)
# colors = cv2.cvtColor(imgL, cv2.COLOR_BGR2RGB)
win_size = 5
min_disp = -1
max_disp = 63 #min_disp * 9
num_disp = max_disp - min_disp # Needs to be divisible by 16
#Create Block matching object. 
stereo = cv2.StereoSGBM_create(minDisparity= min_disp,
 numDisparities = num_disp,
 blockSize = 10,
 uniquenessRatio = 5,
 speckleWindowSize = 5,
 speckleRange = 4,
 disp12MaxDiff = 1,
 P1 = 8*3*win_size**2,#8*3*win_size**2,
 P2 =32*3*win_size**2) #32*3*win_size**2)
#Compute disparity map
print ("\nComputing the disparity  map...")
disparity_map = stereo.compute(imgL, imgR)
plt.imshow(disparity_map,'gray')
plt.show()
