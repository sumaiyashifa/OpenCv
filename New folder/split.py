import cv2 as cv

# Load the image
image_path = r'D:\opencv\pic\bogo1.png'
img_raw = cv.imread(image_path)

# Check if the image was loaded correctly
if img_raw is None:
    print("Error: Could not read the image.")
    exit()

# Split the image into its channels (B, G, R)
b_channel, g_channel, r_channel = cv.split(img_raw)

# Display the individual channels
cv.imshow("Blue Channel", b_channel)
cv.imshow("Green Channel", g_channel)
cv.imshow("Red Channel", r_channel)

# Optional: Modify one of the channels (e.g., set the red channel to zero)
r_channel[:] = 0  # Set all red channel values to zero

# Merge the channels back together
merged_image = cv.merge((b_channel, g_channel, r_channel))

# Display the merged image
cv.imshow("Merged Image", merged_image)
cv.waitKey(0)

# Save the merged image (optional)
cv.imwrite(r'D:\opencv\pic\merged_image.jpeg', merged_image)

# Clean up
cv.destroyAllWindows()
