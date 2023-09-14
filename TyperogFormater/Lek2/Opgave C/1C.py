import cv2 as cv

image = cv.imread("../Opgave E/Dolphin.jpg")
image1 = image.copy()

image1[200,200] = (0,0,255)
image1[201,200] = (0,0,255)
image1[200,201] = (0,0,255)
image1[201,201] = (0,0,255)

#for i in range(0,i,1):
image1[:,300,:] = (0,255,0)

cv.imshow("Dolphin",image1)
cv.imwrite("Dolphin_copy.png",image1)
cv.waitKey(0)
