import cv2
import numpy as np

image = cv2.imread("animal.jpg")
copy_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask_Vert = np.array(([-1,0,1],
                      [-2,0,2],
                      [-1,0,1]))
mask_Vert2 = np.array(([-1,0,1],
                      [-2,0,2],
                      [-1,0,1]))*-1


mask_Hori = np.array(([-1,-2,-1],
                      [0,0,0],
                      [1,2,1]))
mask_Hori2 = np.array(([-1,-2,-1],
                      [0,0,0],
                      [1,2,1]))*-1
img_Vertical_filter = cv2.filter2D(copy_image, -1, mask_Hori)
img_Horizontal_filter = cv2.filter2D(copy_image, -1, mask_Vert)
img_Vertical_filter2 = cv2.filter2D(copy_image, -1, mask_Hori2)
img_Horizontal_filter2 = cv2.filter2D(copy_image, -1, mask_Vert2)


combined_img = cv2.add(img_Vertical_filter, img_Vertical_filter2)
combined_img2 = cv2.add(img_Horizontal_filter, img_Horizontal_filter2)
combined_final = cv2.add(combined_img, combined_img2)

threshold = 80
def stepFunktion(input_intesity,threshold):
    if input_intesity < threshold:
        output_intensity = 0
    else:
        output_intensity = 255
    return output_intensity

binary_vec = np.vectorize(stepFunktion)

# Gray to binary function
img_transformed = binary_vec(combined_final,threshold).astype(np.uint8)

cv2.imshow("Org",image)
cv2.imshow("combined",combined_final)
cv2.imshow("black",img_transformed)
cv2.waitKey(0)
