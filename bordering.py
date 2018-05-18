import numpy as np
import cv2

img = cv2.imread('pink-2254970_1920.jpg')
howmany = 20
size = 10
reflect = []
reflect.append(img)
for i in range(howmany):
	reflect.append(cv2.copyMakeBorder(reflect[i],size, size, size, size ,cv2.BORDER_REFLECT_101))
cv2.imshow('image',reflect[howmany])
cv2.waitKey(5000)
cv2.destroyAllWindows()
