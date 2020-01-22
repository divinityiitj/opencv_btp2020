import cv2

img = cv2.imread('lena.jpg',1)

img =cv2.line(img,(0,0) ,(255,255),(255,0,0),5) #fourth argument is 255 for blue color
img =cv2.arrowedLine(img,(0,255) ,(255,255),(255,0,0),5)

img = cv2.rectangle(img,(384,0),(452,255),(0,0,255),-1)# in -1 last parameter the rectangle gets filled
img = cv2.circle(img, (680,480),56, (0,255,0),0)
cv2.imshow('line',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
