import cv2 as cv

image = cv.imread('binary.png')
grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)



cv.imshow('Black white image', grayImage)

cv.imwrite("Binary_copy.pbm", grayImage)

cv.waitKey(0)
cv.destroyAllWindows()
