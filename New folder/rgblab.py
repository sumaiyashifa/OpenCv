import cv2 as cv

# Load the image
image_path = r'D:\opencv\pic\bogo1.png'
img_raw = cv.imread(image_path)

# Check if the image was loaded correctly
if img_raw is None:
    print("Error: Could not read the image.")
    exit()

# Convert the image from BGR to LAB
lab_image = cv.cvtColor(img_raw, cv.COLOR_BGR2Lab)
cv.imshow("changed",lab_image)
cv.waitKey(0)
cv.destroyAllWindows()
