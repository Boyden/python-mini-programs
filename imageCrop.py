import cv2
import numpy as np

def imageCrop(path, filename, leftup, rightdown):
	img = cv2.imread(path)
	if len(img.shape) == 2:
	    crop_img = np.zeros((rightdown[0]-leftup[0], rightdown[1]-leftup[1]), dtype=np.uint8)
    else:
    	crop_img = np.zeros((rightdown[0]-leftup[0], rightdown[1]-leftup[1], 3), dtype=np.uint8)
    
	for i in range(leftup[0], rightdown[0]):
		for j in range(leftup[1], rightdown[1]):
			crop_img[i-leftup[0], j-leftup[1]] = img[i, j]

	cv2.imwrite(filename, crop_img)
	return crop_img