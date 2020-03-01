from PySimpleGUI import Slider, Window, Image, Button, Text, Column
import numpy as np
import cv2
from matplotlib import pyplot as plt

ImgL = cv2.imread('image_1.png',0)
ImgR = cv2.imread('image_2.png',0)

win_size = 2
min_disp = -1
max_disp = 63 #min_disp * 9
num_disp = max_disp - min_disp # Needs to be divisible by 16

stereo = cv2.StereoSGBM_create(minDisparity= min_disp,
 numDisparities = num_disp,
 blockSize = 11,
 uniquenessRatio = 5,
 speckleWindowSize = 5,
 speckleRange = 4,
 disp12MaxDiff = 1,
 P1 = 8*3*win_size**2,#8*3*win_size**2,
 P2 =32*3*win_size**2) #32*3*win_size**2)

disparity_map = stereo.compute(ImgL, ImgR)

cv2.imwrite('disparity_map.png', disparity_map)

imgL = Image('image_1.png')
imgR = Image('image_2.png')
imgS = Image('disparity_map.png')

btn = Button('Close')

minDisparitytext = Text(text="minDisparity")
numDisparitiestext = Text(text="numDisparities")
blockSizetext = Text(text="blockSize")
uniquenessRatiotext = Text(text="uniquenessRatio")
speckleWindowSizetext = Text(text="speckleWindowSize")
speckleRangetext = Text(text="speckleRange")
disp12MaxDifftext = Text(text="disp12MaxDiff")
P1text = Text(text="P1")
P2text = Text(text="P2")

minDisparity = 		Slider(range=(-1,20), resolution=1, orientation='horizontal', enable_events=True, default_value=-1)
numDisparities = 	Slider(range=(0,96), resolution=1, orientation='horizontal', enable_events=True, default_value=num_disp)
blockSize = 		Slider(range=(0,96), resolution=1, orientation='horizontal', enable_events=True, default_value=11)
uniquenessRatio = 	Slider(range=(5,15), resolution=1, orientation='horizontal', enable_events=True,  default_value=5)
speckleWindowSize = Slider(range=(50,200), resolution=1, orientation='horizontal', enable_events=True,default_value=5)
speckleRange = 		Slider(range=(0,3), resolution=0.1, orientation='horizontal', enable_events=True, default_value=4)
disp12MaxDiff = 	Slider(range=(0,100), resolution=1, orientation='horizontal', enable_events=True, default_value=1)
P1Slider = 	Slider(range=(0,10), resolution=0.1, orientation='horizontal', enable_events=True, default_value=8*3*win_size**2)
P2Slider = 	Slider(range=(0,10), resolution=0.1, orientation='horizontal', enable_events=True, default_value=32*3*win_size**2)


layout = [[imgL, imgR], [Column([[minDisparitytext, minDisparity], 
								 [numDisparitiestext, numDisparities], 
								 [blockSizetext, blockSize], 
								 [uniquenessRatiotext, uniquenessRatio], 
								 [speckleWindowSizetext, speckleWindowSize], 
								 [speckleRangetext, speckleRange], 
								 [disp12MaxDifftext, disp12MaxDiff],
								 [P1text, P1Slider],
								 [P2text, P2Slider],]), imgS], 
								 [btn]]

window = Window("Tweak Stereo Image", layout)

while True:
	event, values = window.read()
	if event in (None, 'Close'):
		break
	else:
		stereo = cv2.StereoSGBM_create(minDisparity= int(values[2]),
										numDisparities = int(values[3]),
										blockSize = int(values[4]),
										uniquenessRatio = int(values[5]),
										speckleWindowSize = int(values[6]),
										speckleRange = int(values[7]),
										disp12MaxDiff = int(values[8]),
										P1 = int(8*3*values[9]**2),#8*3*win_size**2,
										P2 =int(32*3*values[10]**2)) #32*3*win_size**2)	

		disparity_map = stereo.compute(ImgL, ImgR)

		cv2.imwrite('disparity_map.png', disparity_map)
		imgS.update('disparity_map.png')


window.close()