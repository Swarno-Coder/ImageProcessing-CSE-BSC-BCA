import cv2
import matplotlib.pyplot as plt

# Load a gray image
gray_image = cv2.imread('gray_image.jpg', cv2.IMREAD_GRAYSCALE)

# Calculate the histogram
hist = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Display the histogram
plt.hist(gray_image.ravel(), 256, [0, 256])
plt.show()
