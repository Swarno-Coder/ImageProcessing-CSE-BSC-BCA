import cv2

# Load an image
image = cv2.imread('input_image.jpg')

# Increase brightness (adjust gamma value as needed)
gamma = 1.5
brightened_image = np.power(image / 255.0, gamma) * 255.0
brightened_image = np.uint8(brightened_image)

# Decrease brightness (adjust gamma value as needed)
gamma = 0.5
darkened_image = np.power(image / 255.0, gamma) * 255.0
darkened_image = np.uint8(darkened_image)

# Increase contrast (adjust alpha and beta as needed)
alpha = 1.5
beta = 50
contrasted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# Define lower and upper bounds for gray level slicing
lower_bound = 100
upper_bound = 200

# Create a mask for gray level slicing
mask = cv2.inRange(image, lower_bound, upper_bound)

# Apply the mask to the original image
sliced_image = cv2.bitwise_and(image, image, mask=mask)