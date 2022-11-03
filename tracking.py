import cv2 as cv
import numpy as np

img_original = cv.imread("./imagens/4.png")

window = 'img'
colors = [0, 0, 0]


def set_and_change(key, color):
    colors[key] = color
    change()


def change():
    red, green, blue = colors

    print(f'red: {red} green: {green} blue: {blue}')

    img = img_original.copy()
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([red,green,blue])
    mask = cv.inRange(hsv, lower_red, upper_red)
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
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
    
    cv.imshow(window, mask)


if __name__ == '__main__':
    change()

    cv.createTrackbar("red", window, 0, 255, lambda x: set_and_change(0, x))
    cv.createTrackbar("green", window, 0, 255, lambda x: set_and_change(1, x))
    cv.createTrackbar("blue", window, 0, 255, lambda x: set_and_change(2, x))

    cv.waitKey(0)
    cv.destroyAllWindows()
