import cv2 as cv

# Image path to read
image_path = r'D:\opencv\pic\bogo1.png'

# Read the image
image = cv.imread(image_path)

# Check if the image was loaded correctly
if image is None:
    print("Error: Could not read the image.")
else:
    print("Image Data Type:", image.dtype)
    # Access image properties
    height, width, channels = image.shape
    print("Image Dimensions (Height, Width, Channels):", (height, width, channels))
    print("Image Data Type:", image.dtype)

    # Display the image (optional)
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()
