import cv2 as cv
import numpy as np
cap = cv.VideoCapture('C:/Temp/00023.MTS')
while(1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([59, 176, 143])
    upper_blue = np.array([130, 255, 255])
    # Порог изображения HSV для получения только синих цветов
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Побитовая-И-маска и исходное изображение
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()