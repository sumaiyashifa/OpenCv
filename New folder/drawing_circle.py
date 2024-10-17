import cv2 as cv
# Image path to read
# ip = r'D:\opencv\pic\bogo1.png'
# a = cv.imread(ip)
# resize=cv.resize(a,(200,200))
# color=(255,255,255)
# thickness=2
# certer_co=(120,50)

# radius=20
# resize=cv.circle(resize,certer_co,radius,color,thickness)
# cv.imshow('line image',resize)
# cv.waitKey(0)
# cv.destroyAllWindows() 

#rectangle
# ip = r'D:\opencv\pic\bogo1.png'
# a = cv.imread(ip)
# resize=cv.resize(a,(200,200))
# height, width = resize.shape[:2]
# color=(0,0,255)
# thickness=5
# size = 50  # Half-length of the rectangle
# center_x = width // 2
# center_y = height // 2
# startpoint = (center_x - size, center_y - size)
# endpoint = (center_x + size, center_y + size)
# resize=cv.rectangle(resize,startpoint,endpoint,color,thickness)
# cv.imshow('line image',resize)
# cv.waitKey(0)
# cv.destroyAllWindows()

# ellipse
# Load the image
ip = r'D:\opencv\pic\bogo1.png'
a = cv.imread(ip)

# Resize the image (optional)
resize = cv.resize(a, (400, 400))

# Define the center of the ellipse
center = (200, 200)  # (x, y) coordinates

# Define the axes lengths
axes_length = (100, 50)  # (major axis length, minor axis length)

# Define the rotation angle (in degrees)
angle = 30  # Rotate the ellipse 30 degrees

# Define the start and end angle of the arc (in degrees)
start_angle = 0
end_angle = 360  # Full ellipse

# Define the color and thickness of the ellipse
color = (0, 255, 0)  # Green color
thickness = 2  # Line thickness

# Draw the ellipse on the image
cv.ellipse(resize, center, axes_length, angle, start_angle, end_angle, color, thickness)

# Display the image with the ellipse
cv.imshow('Ellipse Image', resize)
cv.waitKey(0)
cv.destroyAllWindows()