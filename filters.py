import cv2

# Load an image
image = cv2.imread('input_image.jpg')

# Apply mean filtering
kernel_size = (5, 5)  # Adjust kernel size as needed
mean_filtered_image = cv2.blur(image, kernel_size)

# Define a custom kernel for weighted average filtering
kernel = np.array([[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]], dtype=np.float32) / 16  # Adjust weights as needed

# Apply weighted average filtering
weighted_average_filtered_image = cv2.filter2D(image, -1, kernel)

# Apply median filtering
kernel_size = 3  # Adjust kernel size as needed (should be odd)
median_filtered_image = cv2.medianBlur(image, kernel_size)

# Apply max/min filtering (max)
max_filtered_image = cv2.erode(image, None, iterations=1)

# Apply max/min filtering (min)
min_filtered_image = cv2.dilate(image, None, iterations=1)