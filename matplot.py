import cv2
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg',-1)

cv2.imshow('image',img) #cv shows in bgr format and matplob shows in rbg format
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #comment this line for rbg format in matplob


plt.imshow(img)
#plt.xticks([],plt.yticks([])) this will hide the axis in img 

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
