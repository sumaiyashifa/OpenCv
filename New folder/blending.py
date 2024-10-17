import cv2 as cv

# Load the foreground image
image_path = r'D:\opencv\pic\bogo1.png'
img_raw = cv.imread(image_path)

# Load the background image
image_path1 = r'D:\opencv\pic\background.jpg'
img_raw1 = cv.imread(image_path1)

# Check if both images were loaded correctly
if img_raw is None or img_raw1 is None:
    print("Error: Could not read one or both of the images.")
    exit()

# Resize both images to the same dimensions
a = cv.resize(img_raw, (800, 600))
b = cv.resize(img_raw1, (800, 600))

# Blend the images using addWeighted
ben = cv.addWeighted(a, 0.6, b, 1, 0)

# Display the blended image
cv.imshow("Blended Image", ben)
cv.waitKey(0)
cv.destroyAllWindows()
