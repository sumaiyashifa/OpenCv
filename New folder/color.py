import cv2 as cv

# Image path to read
ip = r'D:\opencv\pic\bogo1.png'

# Read the image
image = cv.imread(ip)

# Check if the image was loaded correctly
if image is None:
    print("Error: Could not read the image.")
else:
    # Accessing pixel at (100, 100)
    px = image[100, 100]
    print("Pixel value at (100, 100):", px)

    # Accessing the blue channel value at (100, 100)
    blue = image[100, 100, 0]
    print("Blue channel value at (100, 100):", blue)

    # Setting the pixel at (100, 100) to white
    image[100, 100] = [255, 255, 255]
    print("New pixel value at (100, 100):", image[100, 100])

    # Optionally save the modified image
    cv.imwrite(r'D:\opencv\pic\bogo1_modified.png', image)
