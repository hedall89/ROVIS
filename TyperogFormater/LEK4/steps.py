import cv2
import numpy


threshold = 127
def binary(input_intensity, threshold):
    if input_intensity < threshold:
        output_intensity = 0
    else:
        output_intensity = 255

    return output_intensity




binary_vectorized = numpy.vectorize(binary)



