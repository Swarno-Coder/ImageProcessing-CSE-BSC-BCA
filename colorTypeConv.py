import cv2

# Load an image
image = cv2.imread('input_image_rgb.png')

# RGB to gray
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gray to binary
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# RGB to binary
ret, binary_rgb_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# RGB to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# HSV to RGB
rgb_from_hsv_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

# RGB to YCbCr
ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# YCbCr to RGB
rgb_from_ycbcr_image = cv2.cvtColor(ycbcr_image, cv2.COLOR_YCrCb2BGR)


cv2.imshow('Original image', image)
cv2.imshow('Gray image', gray_image)
cv2.imshow('Binary image', binary_image)
cv2.imshow('Binary RGB image', binary_rgb_image)
cv2.imshow('HSV image', hsv_image)
cv2.imshow('RGB from HSV image', rgb_from_hsv_image)
cv2.imshow('YCbCr image', ycbcr_image)
cv2.imshow('RGB from YCbCr image', rgb_from_ycbcr_image)
cv2.waitKey(0)