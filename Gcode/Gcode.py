from PIL import Image
import numpy as np
import cv2 as cv

path = "C:\\Users\\acer\\Desktop\\表情包.jpg"
limit = 120
im = Image.open(path)
im = im.convert("L")
im = im.point(lambda i: i > limit and 255)
img = np.zeros((im.height, im.width, 1), np.uint8)

for i in range(im.height):
	for j in range(im.width):
		img[i, j] = im.getpixel((j, i))

contours = cv.findContours(img, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

img = np.zeros((im.height, im.width, 1), np.uint8)
cv.drawContours(img, contours[1][:-1], -1, (255, 255, 255), 1)

for i in range(im.height):
	for j in range(im.width):
		if img[i, j] == 0:
			im.putpixel((j, i), 255)
		else:
			im.putpixel((j, i), 0)

contours = contours[1][:-1]
path = path[:-4] + ".nc"
f = open(path, 'wt')
f.write("M5\n")
f.write("G0 Z%f\n"%6) 
for contour in contours:
    f.write("G0 X%f Y%f\n" % ((contour[0][0][1] * 6), (contour[0][0][0] * 6)))
    f.write("M3\n")
	f.write("G0 Z%f\n"%-1)
    for con in contour:
        f.write("G0 X%f Y%f\n" % ((con[0][1] * 6), (con[0][0] * 6)))
    
    f.write("G0 Z%f\n"%6)
    f.write("M5\n")

f.write("G0 X0 Y0\n")
f.close()
