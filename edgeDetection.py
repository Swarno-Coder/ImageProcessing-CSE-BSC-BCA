import cv2
import numpy as np
# Load a grayscale image
gray_image = cv2.imread('input_image.png', cv2.IMREAD_GRAYSCALE)

# Apply the difference operator
difference_image = cv2.Laplacian(gray_image, cv2.CV_64F)

# Display the difference edge image
cv2.imshow('Difference Edge Image', difference_image)
cv2.waitKey(0)


# Apply the Robert operator
robert_x = cv2.filter2D(gray_image, -1, np.array([[-1, 0], [0, 1]]))
robert_y = cv2.filter2D(gray_image, -1, np.array([[0, -1], [1, 0]]))
robert_edge_image = cv2.addWeighted(robert_x, 0.5, robert_y, 0.5, 0)

# Display the Robert edge image
cv2.imshow('Robert Edge Image', robert_edge_image)
cv2.waitKey(0)

