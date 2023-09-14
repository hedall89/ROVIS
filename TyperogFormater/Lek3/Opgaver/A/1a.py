from matplotlib import pyplot
import cv2 as cv




def plotHist(im):
    histogram = im.ravel()
    pyplot.hist(histogram, 256, [0, 255])
    pyplot.show()

image = cv.imread("Tower.png",0)

plotHist(image)
#2b
light_copy = image.copy()
light_value = 35

light_copy = cv.add(light_copy, light_value)

plotHist(light_copy)

#3b
dark_value = -35
dark_copy = image.copy()
dark_copy = cv.add(dark_copy,dark_value)

plotHist(dark_copy)







