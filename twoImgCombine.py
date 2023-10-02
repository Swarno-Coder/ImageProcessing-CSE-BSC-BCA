lena_image = cv2.imread('.bin', cv2.IMREAD_GRAYSCALE)
peppers_image = cv2.imread('peppers.bin', cv2.IMREAD_GRAYSCALE)

# Ensure both images have the same dimensions (256x256)
if lena_image.shape == peppers_image.shape == (256, 256):
    # Create a new 256x256 image J as specified
    J = np.zeros((256, 256), dtype=np.uint8)
    J[:, :128] = lena_image[:, :128]
    J[:, 128:] = peppers_image[:, 128:]
    
    # Show the resulting image J
    cv2.imshow('Combined Image J', J)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Both 'lena.bin' and 'peppers.bin' images should have dimensions of 256x256.")