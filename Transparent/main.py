import cv2
import numpy as np

image=cv2.imread("Transparent/input/result.jpg")
Gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
_,alpha = cv2.threshold(Gray_image,80,255,cv2.THRESH_BINARY)
b, g, r = cv2.split(image)

bgra = [b,g,r, alpha]
dst = cv2.merge(bgra,4)

cv2.imwrite("Transparent/output/result.png",dst)
cv2.waitKey()