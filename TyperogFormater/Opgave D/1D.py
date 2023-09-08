import cv2 as cv

image = cv.imread("Mountain.png")
copy = image.copy()

shape = copy.shape
height = shape[0]
width = shape[1]










for i in range(0,width,2):
    for j in range(0,height,2):
        copy[j, i, :] = (0, 0, 0)

for k in range(1,width,2):
    for h in range(1,height,2):
        copy[h, k, :] = (0, 0, 0)









cv.imshow("Mountain_copy",copy)
cv.waitKey(0)
cv.imwrite("Copy_line.png", copy)