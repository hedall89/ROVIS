import cv2
import numpy as np

image = cv2.imread("landscape.png")
copy_img = image.copy()
gamma = 0.5

def gammeCorrection(input_intensity, gamma_value):
    output_intensity = 255 * (input_intensity / 255) ** gamma_value
    return output_intensity



gamma_correction_vec = np.vectorize(gammeCorrection)
img_transformed = gamma_correction_vec(copy_img,gamma).astype(np.uint8)



cv2.imshow("Original", image)
cv2.imshow("GammaCorrection", img_transformed)

cv2.waitKey(0)