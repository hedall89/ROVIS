import cv2
import numpy as np
from matplotlib import pyplot as plt


def fremHaev(pix, r1, s1, r2, s2):
    if (0 <= pix and pix <= r1):
        return (s1 / r1) * pix
    elif (r1 < pix and pix <= r2):
        return ((s2 - s1) / (r2 - r1)) * (pix - r1) + s1
    else:
        return ((255 - s2) / (255 - r2)) * (pix - r2) + s2

img = cv2.imread('bacteria.jpg')

r1 = 80
s1 = 40
r2 = 140
s2 = 220

# Vectorize the function to apply it to each value in the Numpy array.
contrast_vec = np.vectorize(fremHaev)


contrast = contrast_vec(img, r1, s1, r2, s2).astype(np.uint8)



x = np.arange(0, 255, 1) # Create array from 0 to 254 with stepsize 1
y = contrast_vec(x,r1,s1,r2,s2) # Send all values of x to function to calculate y
plt.axes(xlim=(0,300), ylim=(-10, 300))
plt.ylabel('Output image')            # y-label
plt.xlabel('Input image')            # x-label

plt.title('piece-wise Transformation')    # Graph title
plt.legend('Transformation Line')
plt.plot(x,y)
plt.show()


cv2.imshow("contrast",contrast)
cv2.imshow("Original", img)
cv2.waitKey(0)