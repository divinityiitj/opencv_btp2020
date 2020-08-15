import cv2 as cv
import numpy as np 

img = cv.imread('gradient.png',0) #_, is a variable name
_, th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)#binary threshhold 
_, th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)#inverses the value 

cv.imshow('image',img)
cv.imshow('TH1',th1)
cv.imshow('TH2',th2)
cv.waitKey(0)
cv.destroyAllWindows()

