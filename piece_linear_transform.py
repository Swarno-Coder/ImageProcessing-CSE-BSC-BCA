import cv2
import numpy as np

# Load a grayscale image
gray_image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply piecewise linear transformation
piecewise_transformed_image = np.piecewise(gray_image, [gray_image <= 127, gray_image > 127], [lambda x: 2*x, lambda x: 255-2*(255-x)])
piecewise_transformed_image = np.uint8(piecewise_transformed_image)
