7#color detection
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

ip = r'D:\opencv\pic\bogo1.png'
a = cv.imread(ip)
hsv=cv.cvtColor(a,cv.COLOR_BGR2HSV)
# l_b=np.array([0,50,50])
# u_b=np.array([130,255,225])
l_b=np.array([10,100,20])#sudhu yellow color daoa ongsho dekhte pabo
u_b=np.array([25,255,225])
m_bb=cv.inRange(hsv,l_b,u_b)
res=cv.bitwise_and(a,a,mask=m_bb)
cv.imshow('rees',res)
cv.waitKey(0)
cv.destroyAllWindows()