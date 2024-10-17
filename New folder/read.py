import cv2 as cv

# Image path to read
ip = r'D:\opencv\pic\bogo1.png'
a = cv.imread(ip)

# Display the image in a window
cv.imshow('sample image', a)

# Wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()

# Directory and filename to save the image
directory = r'D:\opencv\pic'
filename = 'savedPic.png'

# Full path for the saved image
full_path = f"{directory}\\{filename}"

# Save the image
cv.imwrite(full_path, a)
print(f'Image saved at {full_path}')

print(a.shape)


#rgb


