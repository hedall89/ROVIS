import cv2 as cv

image = cv.imread("red_circle.png")
copy = image.copy()

shape = copy.shape
width = shape[1]
height = shape[0]

print(height, width)

center_coordinater = (width,1)
radius = 100
color = (0,255,255)
thickness = -1


start_point = (340,195)
end_point = (width,195)
color2 = (255,0,0)
thickness2 = 5

copy = cv.circle(copy,center_coordinater,radius,color,thickness)
copy = cv.line(copy,start_point,end_point,color2,thickness2)


cv.imshow("yellow_corner",copy)
cv.waitKey(0)