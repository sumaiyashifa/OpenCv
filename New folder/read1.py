import cv2 as cv
# Image path to read
ip = r'D:\opencv\pic\bogo1.png'
a = cv.imread(ip)
# gray color a cange korlam
gray=cv.cvtColor(a,cv.COLOR_BGR2GRAY)
#resize korbo
resize=cv.resize(a,(200,200))

# cv.imshow('original image',a)
#  cv.imshow('gray image',gray)
# cv.imshow('resized image',resize)
# cv.waitKey(0)
# cv.destroyAllWindows()





# complex,duplex,triplex
# textreturn,starting point,name of the font,mplex,size,color,thickness
text="i love you"
coordinates=(100,100)
font=cv.FONT_HERSHEY_SIMPLEX
fontScale=1
color=(255,0,0)
thicknes=2
a=cv.putText(a,text,coordinates,font,fontScale,color,thicknes)
cv.imshow('resized image',a)
cv.waitKey(0)
cv.destroyAllWindows()
