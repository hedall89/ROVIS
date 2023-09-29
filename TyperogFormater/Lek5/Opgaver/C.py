import cv2
import numpy as np

image = cv2.imread("animal.jpg")
copy_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


Canny_img = cv2.GaussianBlur(copy_image, (5,5), 7)
#canny_image = cv2.Canny(copy_image,50,155)
canny_image = cv2.Canny(Canny_img,70,100)



cv2.imshow("Org", image)
cv2.imshow("Canny", canny_image)
cv2.waitKey(0)
