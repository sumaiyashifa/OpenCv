import cv2 as cv
import numpy as np

# Load the image
image_path = r'D:\opencv\pic\bogo1.png'
a = cv.imread(image_path)
img_raw=cv.resize(a,(200,200))

# Check if the image was loaded correctly
if img_raw is None:
    print("Error: Could not read the image.")
    exit()

# Define a sharpening kernel
sharpening_kernel = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])

# Apply the sharpening kernel to the image
sharpened_image = cv.filter2D(img_raw, -1, sharpening_kernel)

# Display the original and sharpened images
cv.imshow("Original Image", img_raw)
cv.imshow("Sharpened Image", sharpened_image)
cv.waitKey(0)
cv.destroyAllWindows()

