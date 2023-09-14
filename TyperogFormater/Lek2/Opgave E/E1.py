import cv2 as cv

image = cv.imread("Dolphin.jpg")

copy = image.copy()
shape = copy.shape

height = int(shape[0] * 50 / 100)
width = int(shape[1] * 50 / 100)

dimension = (width,height)
resized_image = cv.resize(image, dimension, interpolation = cv.INTER_AREA)

cv.imshow("image",image)
cv.imshow("resized",resized_image)
cv.imwrite("resized_Dolphin.png", resized_image)

cv.waitKey(0)




