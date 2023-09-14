import Histogram
import cv2
from matplotlib import pyplot

image = cv2.imread("robot_arm.jpg")

def splitColors(image):

    b,g,r = cv2.split(image)
    Histogram.plotHist(b)
    Histogram.plotHist(g)
    Histogram.plotHist(r)



#splitColors(image)




