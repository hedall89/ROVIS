import cv2
import numpy as np


image = cv2.imread("animal.jpg")
copy = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask_Hori = np.array(([0,1,0],
                      [1,4,1],
                      [0,1,0]))
mask_Vert = np.array(([0,-0,0],
                      [-1,4,-1],
                      [0,-1,0]))

img_Horizontal_filter = cv2.Laplacian(copy,-1, mask_Hori)
img_Vertical_filter = cv2.Laplacian(copy,-1, mask_Vert)


combined_img = cv2.add(img_Horizontal_filter, img_Vertical_filter)

cv2.imshow("black",combined_img)
cv2.waitKey(0)
