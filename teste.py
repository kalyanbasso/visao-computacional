import cv2 as cv
import numpy as np
from time import sleep


# frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
# frame = cv.GaussianBlur(frame, (5, 5), 0)

captura = cv.VideoCapture("./video/video-chao.mp4")

while(1):
    ret, frame = captura.read()
    # sleep(1)
    frame = cv.flip(frame, 0) 
    # find red retangle
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([10,255,255])
    mask = cv.inRange(hsv, lower_red, upper_red)
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 30:
            cv.drawContours(frame, [cnt], 0, (0, 255, 0), 3)
            M = cv.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(frame,'Centro',(cx-20,cy-20), font, 0.5,(255,255,255),2,cv.LINE_AA)
    cv.imshow('frame',hsv)
    cv.imshow('mask',mask)
    # k = cv.waitKey(5) & 0xFF
    # if k == 27:
    #     break
    
    # edges = cv.Canny(frame, threshold1=30, threshold2=100)
    # cv.imshow("Video", frame)
    
    
   
    k = cv.waitKey(30) & 0xff
    if k == 'ESC':
        print("macacoooooooo")
        break

captura.release()       
cv.destroyAllWindows()
