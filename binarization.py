import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
  pass

def calcAndDrawHist(image, color):  
    hist= cv2.calcHist([image], [0], None, [256], [0.0,255.0])  
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)  
    histImg = np.zeros([256,256,3], np.uint8)  
    hpt = int(0.9* 256);  
      
    for h in range(256):  
        intensity = int(hist[h]*hpt/maxVal)  
        cv2.line(histImg,(h,256), (h,256-intensity), color)  
          
    return histImg; 


cv2.namedWindow('Binarization')

wnd = 'Binarization'
cv2.createTrackbar("Max", wnd,0,255,nothing)
cv2.setTrackbarPos('Max',wnd, 255)
cv2.createTrackbar("Min", wnd,0,255,nothing)

img = cv2.imread('1322499.png')

b, g, r = cv2.split(img)  

histImgB = calcAndDrawHist(b, [255, 0, 0])  
histImgG = calcAndDrawHist(g, [0, 255, 0])  
histImgR = calcAndDrawHist(r, [0, 0, 255])  


# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
# titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# for i in xrange(6):
#     plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
while(1):
   max_val = cv2.getTrackbarPos("Max", "Binarization")
   min_val = cv2.getTrackbarPos("Min", "Binarization")
   show_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
   show_img[show_img<min_val] = 0
   show_img[show_img>max_val] = 0

   cv2.imshow("Binarization",show_img)
   cv2.imshow("histImgB", histImgB)  
   cv2.imshow("histImgG", histImgG)  
   cv2.imshow("histImgR", histImgR)  

   k = cv2.waitKey(1) & 0xFF

   if k == ord('m'):
     mode = not mode
   elif k == 27:
     break
cv2.destroyAllWindows()