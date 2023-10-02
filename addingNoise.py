import cv2
import numpy as np

# Load an image
image = cv2.imread('input_image_rgb.png')

# Add salt and pepper noise
noise_density = 0.02  # Adjust as needed
salt_and_pepper_noise = np.random.choice([0, 255], size=image.shape, p=[1 - noise_density, noise_density])
print(salt_and_pepper_noise.shape, image.shape)
noisy_image = cv2.multiply(image, salt_and_pepper_noise)

# Display the noisy image
cv2.imshow('Noisy Image (Salt and Pepper)', noisy_image)
cv2.waitKey(0)

# Add Gaussian noise
mean = 0
stddev = 25  # Adjust as needed
gaussian_noise = np.random.normal(mean, stddev, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, gaussian_noise)

# Display the noisy image
cv2.imshow('Noisy Image (Gaussian)', noisy_image)
cv2.waitKey(0)
cv2.destroyAllWindows()