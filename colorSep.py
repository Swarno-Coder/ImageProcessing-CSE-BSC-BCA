import cv2

# Load a color image
color_image = cv2.imread('input_image_rgb.png')

# Split into R, G, and B channels
b, g, r = cv2.split(color_image)

cv2.imshow('red', r)
cv2.imshow('green', g)
cv2.imshow('blue', b)
    
cv2.waitKey(0)