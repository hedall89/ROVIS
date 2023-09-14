from matplotlib import pyplot
import cv2 as cv


def plotHist(im):
    histogram = im.ravel()
    pyplot.hist(histogram, 256, [0, 255])
    pyplot.show()

#image = cv.imread("robot_arm.pgm")

#plotHist(image)


image_map = cv.imread("map.jpg",0)

copy = cv.equalizeHist(image_map)

cv.imshow("map", image_map)
cv.imshow("copy", copy)
cv.waitKey(0)








