import cv2

# Load an image
image = cv2.imread('input_image.png')

# Rotate clockwise
clockwise_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate anti-clockwise
anti_clockwise_image = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Display the rotated images
cv2.imshow('Clockwise', clockwise_image)
cv2.imshow('Anti-Clockwise', anti_clockwise_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
