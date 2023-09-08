import cv2 as cv

image = cv.imread("resized_Dolphin.png")
copy = image.copy()

center_coordinater = (262,58)
radius = 10
color = (0,0,255)
thickness = 2

copy = cv.circle(copy,center_coordinater,radius,color,thickness)
cv.imwrite("red_circle.png",copy)



cv.imshow("circle",copy)
cv.waitKey(0)
