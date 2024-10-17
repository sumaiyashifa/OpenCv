import cv2 as cv

# Load the image
image_path = r'D:\opencv\pic\bogo1.png'
img_raw = cv.imread(image_path, cv.IMREAD_GRAYSCALE)  # Load as grayscale

# Check if the image was loaded correctly
if img_raw is None:
    print("Error: Could not read the image.")
    exit()

# Simple Thresholding
_, simple_threshold = cv.threshold(img_raw, 127, 255, cv.THRESH_BINARY)

# Otsu's Thresholding
_, otsu_threshold = cv.threshold(img_raw, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

# Adaptive Thresholding
adaptive_threshold = cv.adaptiveThreshold(img_raw, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                           cv.THRESH_BINARY, 11, 2)

# Display the original and thresholded images
cv.imshow("Original Image", img_raw)
cv.imshow("Simple Threshold", simple_threshold)
cv.imshow("Otsu's Threshold", otsu_threshold)
cv.imshow("Adaptive Threshold", adaptive_threshold)

cv.waitKey(0)
cv.destroyAllWindows()

