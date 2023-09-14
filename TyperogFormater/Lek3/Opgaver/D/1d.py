import cv2
import numpy

image = cv2.imread("Bolde.jpeg")



HSV_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
#GUL isoleret
lower_bound = numpy.array([20, 50, 50])
upper_bound = numpy.array([35, 255, 255])

mask = cv2.inRange(HSV_image, lower_bound, upper_bound)
res = cv2.bitwise_and(image, image, mask= mask)
#cv2.imshow("wooow",mask)
cv2.imshow("Gul", res)


#Grøn isoleret
lower_bound_green = numpy.array([40, 50, 50])
upper_bound_green = numpy.array([70, 255, 255])

mask_Green = cv2.inRange(HSV_image, lower_bound_green, upper_bound_green)
res_Green = cv2.bitwise_and(image, image, mask= mask_Green)
cv2.imshow("Green",res_Green)


#Rød isoleret
lower_bound_red1 = numpy.array([0, 50, 50])
upper_bound_red1 = numpy.array([7, 255, 255])
lower_bound_red2 = numpy.array([160, 50,50])
upper_bound_red2 = numpy.array([180, 255, 255])


mask_red1 = cv2.inRange(HSV_image, lower_bound_red1, upper_bound_red1)
mask_red2 = cv2.inRange(HSV_image,lower_bound_red2,upper_bound_red2)
mask_red = cv2.add(mask_red1,mask_red2)
res_red = cv2.bitwise_and(image, image, mask= mask_red)
cv2.imshow("red", res_red)



#Blå isoleret

lower_bound_blue = numpy.array([95, 50, 50])
upper_bound_blue = numpy.array([130, 255, 255])

mask_blue = cv2.inRange(HSV_image, lower_bound_blue, upper_bound_blue)
res_blue = cv2.bitwise_and(image, image, mask= mask_blue)

cv2.imshow("blue", res_blue)


combined = cv2.add(res, res_blue)
combined = cv2.add(combined,res_red)
combined = cv2.add(combined, res_Green)
cv2.imshow("combined", combined)
cv2.waitKey(0)


