import cv2
import numpy as np

# Load a grayscale image
gray_image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply power law transformation (gamma correction)
gamma = 0.5  # Adjust gamma value as needed
power_law_transformed_image = np.power(gray_image / 255.0, gamma) * 255.0
power_law_transformed_image = np.uint8(power_law_transformed_image)
