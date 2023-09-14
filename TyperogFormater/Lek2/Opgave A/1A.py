
import cv2 as cv


image = cv.imread('parrot.png')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)


# til at vise billeder
cv.imshow("Original billede", image)
cv.imshow("Gray billede", gray)

cv.imwrite("Parrot_copy.png", gray)


cv.waitKey(0)
cv.destroyAllWindows()





