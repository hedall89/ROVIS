import cv2
import numpy as np

img = cv2.imread("apple.jpg")
img2 = cv2.imread("j_noisy.png")
img2_copy = img2.copy()
img_copy = img.copy()

mask_Vert = np.array(([-1,0,1],
                      [-1,0,1],
                      [-1,0,1]))

mask_Hori = np.array(([-1,-1,-1],
                      [0,0,0],
                      [1,1,1]))

img_Vertical_filter = cv2.filter2D(img_copy, -1, mask_Hori)
img_Horizontal_filter = cv2.filter2D(img_copy, -1, mask_Vert)

Canny_img = cv2.GaussianBlur(img_copy, (7,7), 7)
canny_img = cv2.Canny(Canny_img, 0, 220)

combined_img = cv2.add(img_Horizontal_filter,img_Vertical_filter)


#cv2.imshow("Org", canny_img)
#cv2.imshow("Hori", img_Horizontal_filter)
#cv2.imshow("Vertical", img_Vertical_filter)
#cv2.imshow("combined", combined_img)

kernel = np.ones((2,2),np.uint8)

#img2_erode = cv2.erode(img2_copy,None)
#img3_dilate = cv2.dilate(img2_copy,None)

img2_erode = cv2.erode(img2_copy,kernel, iterations= 4)
img3_dilate = cv2.dilate(img2_copy,kernel, iterations=5)

cv2.imshow("reg",img2_erode)
cv2.imshow("reg3",img3_dilate)
cv2.waitKey(0)