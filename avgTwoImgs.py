import cv2

# Load two images of the same size
image1 = cv2.imread('image1.jpg')
image2 = cv2.imread('image2.jpg')

# Ensure both images have the same dimensions
if image1.shape == image2.shape:
    # Calculate the average of the two images
    averaged_image = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
    
    # Display the new image
    cv2.imshow('Averaged Image', averaged_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Both images should have the same dimensions for averaging.")
