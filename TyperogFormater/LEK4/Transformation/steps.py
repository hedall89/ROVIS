import cv2
import numpy as np

mask = np.array(([1,1,1],
                 [1,10,1],
                 [1,1,1]))*1/18

img = cv2.imread("ladybug.png")
img_copy = img.copy()

img_filter = cv2.filter2D(img_copy, -1, mask)


cv2.imshow("org", img)
cv2.imshow("Mask", img_filter)
cv2.waitKey(0)


