import cv2

# Load a grayscale image
gray_image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Set a threshold value (adjust as needed)
threshold_value = 128

# Apply binary thresholding
ret, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)

# Display the binary segmented image
cv2.imshow('Binary Segmented Image', binary_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
