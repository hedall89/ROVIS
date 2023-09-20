import cv2
import numpy

image1 = cv2.imread("ball_size1.png")
image2 = cv2.imread("ball_size2.png")
image3 = cv2.imread("ball_size3.png")


gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(gray1,127,255,0)
ret1,thresh1 = cv2.threshold(gray2,127,255,0)
ret2,thresh2 = cv2.threshold(gray3,127,255,0)

ball1 = cv2.countNonZero(thresh)
ball2 = cv2.countNonZero(thresh1)
ball3 = cv2.countNonZero(thresh2)

print(ball1)
print(ball2)
print(ball3)

if ball1 < ball2 and ball1 < ball3:
    cv2.imshow("Biggest ball is Image 1",image1)
elif ball2 < ball3:
    cv2.imshow("Biggest ball is Image 2",image2)
else:
    cv2.imshow("Biggest ball is Image 3",image3 )

#til at checke sort hvid billeder om de er korrekte
#cv2.imshow("Biggest ball is Image 1",thresh)
#cv2.imshow("Biggest ball is Image 3",thresh2)
#cv2.imshow("Biggest ball is Image 2",thresh1)

cv2.waitKey(0)