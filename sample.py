import cv2

img = cv2.imread('sample1.jpg',-1)

#print(img)

cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF #0xff is a mask for 64 bit windows
if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('sample-1.jpg',img)
    cv2.destroyAllWindows()

