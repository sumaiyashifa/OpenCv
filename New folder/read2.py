# line function
# import cv2 as cv
# # Image path to read
# ip = r'D:\opencv\pic\bogo1.png'
# a = cv.imread(ip)
# resize=cv.resize(a,(200,200))
# color=(255,255,255)
# thickness=2
# startpoint=(100,100)
# endp=(250,250)
# resize=cv.line(resize,startpoint,endp,color,thickness)
# cv.imshow('line image',resize)
# cv.waitKey(0)
# cv.destroyAllWindows()



#rgb
import cv2 as cv

# Image path to read
ip = r'D:\opencv\pic\bogo1.png'
a = cv.imread(ip,0)

# Display the image in a window
cv.imshow('sample image', a)

# Wait for a key press and close the window
cv.waitKey(0)
cv.destroyAllWindows()
