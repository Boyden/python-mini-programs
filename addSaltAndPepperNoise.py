import cv2
import numpy as np
from numpy import random
def SaltAndPepper(src,percetage):

    NoiseImg=np.copy(src)
    NoiseNum=int(percetage*src.shape[0]*src.shape[1])

    for i in range(NoiseNum):
        randX=random.randint(0,src.shape[0]-1)
        randY=random.randint(0,src.shape[1]-1)
        if random.randint(0,1)==0:
            NoiseImg[randX,randY]=0
        else:
            NoiseImg[randX,randY]=255   

    return NoiseImg 
    
if __name__=='__main__':
    
    img=cv2.imread('Lena.jpg',flags=0)
    gimg=cv2.GaussianBlur(img,(7,7),sigmaX=0)
    NoiseImg=SaltAndPepper(gimg,0.4)

    Pers=[0.4,0.5,0.6]
    for i in Pers:
        NoiseImg=SaltAndPepper(gimg,i)
        fileName='GaussianSaltPepper'+str(i)+'.jpg'
        cv2.imwrite(fileName,NoiseImg,[cv2.IMWRITE_JPEG_QUALITY,100])

    cv2.imshow('img2',NoiseImg)
    cv2.waitKey()