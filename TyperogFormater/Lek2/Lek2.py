import cv2

image = cv2.imread("fancy_fan.png")
image1 = image.copy()


dimensions = image1.shape
print(dimensions)

height = image1.shape[0]
width = image1.shape[1]
print(height)
print(width)

#ændre farve på et pixel til hvid.
for i in range(0,200,1):
    image1[200,i,:] = 255

cv2.imshow("Fancy_fan",image1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("fancy_copy.png", image1)


