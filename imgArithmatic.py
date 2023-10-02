import cv2

# Load two images of the same size
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Ensure both images have the same dimensions
if image1.shape == image2.shape:
    # Image Addition
    addition_result = cv2.add(image1, image2)
    
    # Image Subtraction
    subtraction_result = cv2.subtract(image1, image2)
    
    # Image Multiplication
    multiplication_result = cv2.multiply(image1, image2, scale=1.0)
    
    # Image Division
    division_result = cv2.divide(image1, image2, scale=1.0)
    
    # Display the results
    cv2.imshow('Addition Result', addition_result)
    cv2.imshow('Subtraction Result', subtraction_result)
    cv2.imshow('Multiplication Result', multiplication_result)
    cv2.imshow('Division Result', division_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Both images should have the same dimensions for arithmetic operations.")
