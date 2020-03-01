import cv2

video_capture = cv2.VideoCapture(0)


while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()
	cv2.imwrite("image_2.png", frame)
	break
	try:
		cv2.imshow('Video', frame)
	except Exception as e:
		print(e)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break