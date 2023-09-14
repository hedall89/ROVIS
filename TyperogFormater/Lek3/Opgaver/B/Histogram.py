from matplotlib import pyplot

def plotHist(im):
    histogram = im.ravel()
    pyplot.hist(histogram, 256, [0, 255])
    pyplot.show()