import cv2 as cv
import numpy as np

img_original = cv.imread("./imagens/chao2.png")

red = 0
green = 0
blue = 0


def changeRed(x):
    red = x
    change()
def changeGreen(x):
    green = x
    change()
def changeBlue(x):
    blue = x
    change()

def change():
    img = img_original.copy()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([red,green,blue])
    mask = cv.inRange(hsv, lower_red, upper_red)
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area > 30:
            cv.drawContours(img, [cnt], 0, (0, 255, 0), 3)
            M = cv.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(img, (cx, cy), 7, (255, 255, 255), -1)
            font = cv.FONT_HERSHEY_SIMPLEX
            cv.putText(img,'Centro',(cx-20,cy-20), font, 0.5,(255,255,255),2,cv.LINE_AA)
    cv.imshow('img',mask)

# cv.imshow("img", img_original)
change()

cv.createTrackbar("red", "img", 0, 255, changeRed)
cv.createTrackbar("green", "img", 0, 255, changeGreen)
cv.createTrackbar("blue", "img", 0, 255, changeBlue)

cv.waitKey(0)
cv.destroyAllWindows()