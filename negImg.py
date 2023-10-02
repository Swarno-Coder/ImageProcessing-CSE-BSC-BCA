import cv2

# Load an image
image = cv2.imread('input_image.jpg')

# Calculate image negative
negative_image = 255 - image
