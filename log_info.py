import cv2
import numpy as np

# Load a grayscale image
gray_image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply log transformation
c = 255 / np.log(256)
log_transformed_image = c * (np.log(gray_image + 1))
log_transformed_image = np.uint8(log_transformed_image)
