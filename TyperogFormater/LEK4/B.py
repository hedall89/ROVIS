import matplotlib.pyplot as plt
import cv2
import numpy as np

threshold = 55
green_threshold = 130

def stepFunktion(input_intesity,threshold):
    if input_intesity < threshold:
        output_intensity = 0
    else:
        output_intensity = 255
    return output_intensity



# Load color picture
img = cv2.imread('digital_finger_print.jpg', cv2.IMREAD_COLOR)
img_copy = img.copy()

img_green = img.copy()
# Converting color image to grayscale image
gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)

# Vectorize function
binary_vec = np.vectorize(stepFunktion)

# Gray to binary function
img_transformed = binary_vec(gray,threshold).astype(np.uint8)
# Original image to binary function
img_col_transformed = binary_vec(img,threshold).astype(np.uint8)
img_green[img_transformed == 255] = [57,255,20]

cv2.imshow('original', img)
cv2.imshow('img_gray_transformed', img_transformed)
cv2.imshow('image Green', img_green)
#cv2.imshow('img_col_transformed', img_col_transformed)

# Til at plot funktionen.
x = np.arange(0, 255, 1) # Create array from 0 to 254 with stepsize 1
y = binary_vec(x,threshold) # Send all values of x to function to calculate y
plt.axes(xlim=(0,300), ylim=(-10, 300))
plt.ylabel('Output image')            # y-label
plt.xlabel('Input image')            # x-label

plt.title('Binary transformation')    # Graph title
plt.legend('Transformation Line')
plt.plot(x,y)
plt.show()
