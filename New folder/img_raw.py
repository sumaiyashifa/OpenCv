import cv2 as cv
import numpy as np

# Load the image
image_path = r'D:\opencv\pic\bogo1.png'
img_raw = cv.imread(image_path)

# Check if the image was loaded correctly

roi=cv.selectROI(img_raw)
print(roi)

    # Set the ROI to a specific color (e.g., red)
roi_cropped= img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])] # BGR format for red

    # Optionally, display the modified image
cv.imshow("Modified Image", roi_cropped)
cv.imwrite(r'D:\opencv\pic\c.jpeg', roi_cropped)
cv.waitKey(0)
cv.destroyAllWindows()

    # Save the modified image (optional)
   
