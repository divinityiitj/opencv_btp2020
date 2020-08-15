import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('xray_femur.jpeg',0)
edges = cv2.Canny(img,50,100)
cv2.imshow('image',edges)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
#plt.subplot(121),plt.imshow(img,cmap = 'gray')
#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(edges,cmap = 'gray')
#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

#plt.show()
