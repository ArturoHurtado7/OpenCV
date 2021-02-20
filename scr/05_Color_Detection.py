import cv2
import numpy as np

#HSV
#Hue|Saturation|Value
#Matiz|Saturación|Brillo

#https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv?lq=1
#H: 0-179
#S: 0-255
#V: 0-255

# Blue Mask
# H: 115-135
# S: 100-241
# V:  60-245

# Yellow Mask
# H:  10- 30
# S:  49-255
# V: 222-255

def Trackbar_H1(x):
    print(x)
    if cv2.getTrackbarPos('LH1', 'Trackbar_1') == cv2.getTrackbarPos('LH2', 'Trackbar_2'):
        cv2.setTrackbarPos('LH2', 'Trackbar_2', cv2.getTrackbarPos('LH1', 'Trackbar_1'))
    if cv2.getTrackbarPos('UH1', 'Trackbar_1') == cv2.getTrackbarPos('UH2', 'Trackbar_2'):
        cv2.setTrackbarPos('UH2', 'Trackbar_2', cv2.getTrackbarPos('UH1', 'Trackbar_1'))

def Trackbar_S1(x):
    print(x)
    cv2.setTrackbarPos('LS2', 'Trackbar_2', cv2.getTrackbarPos('LS1', 'Trackbar_1'))
    cv2.setTrackbarPos('US2', 'Trackbar_2', cv2.getTrackbarPos('US1', 'Trackbar_1'))

def Trackbar_V1(x):
    print(x)
    cv2.setTrackbarPos('LV2', 'Trackbar_2', cv2.getTrackbarPos('LV1', 'Trackbar_1'))
    cv2.setTrackbarPos('UV2', 'Trackbar_2', cv2.getTrackbarPos('UV1', 'Trackbar_1'))

def Trackbar_2(x):
    print(x)

cv2.namedWindow('Trackbar_1', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('LH1', 'Trackbar_1', 0, 179, Trackbar_H1)
cv2.createTrackbar('UH1', 'Trackbar_1', 179, 179, Trackbar_H1)
cv2.createTrackbar('LS1', 'Trackbar_1', 0, 255, Trackbar_S1)
cv2.createTrackbar('US1', 'Trackbar_1', 255, 255, Trackbar_S1)
cv2.createTrackbar('LV1', 'Trackbar_1', 0, 255, Trackbar_V1)
cv2.createTrackbar('UV1', 'Trackbar_1', 255, 255, Trackbar_V1)

cv2.namedWindow('Trackbar_2', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('LH2', 'Trackbar_2', 0, 179, Trackbar_2)
cv2.createTrackbar('UH2', 'Trackbar_2', 179, 179, Trackbar_2)
cv2.createTrackbar('LS2', 'Trackbar_2', 0, 255, Trackbar_2)
cv2.createTrackbar('US2', 'Trackbar_2', 255, 255, Trackbar_2)
cv2.createTrackbar('LV2', 'Trackbar_2', 0, 255, Trackbar_2)
cv2.createTrackbar('UV2', 'Trackbar_2', 255, 255, Trackbar_2)

img = cv2.imread('Photos/maimy.jpg',1)
frameHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#cv2.imshow('frameHSV', frameHSV)
cv2.imshow('Img', img)

while True:

    LH1 = cv2.getTrackbarPos('LH1', 'Trackbar_1')
    LS1 = cv2.getTrackbarPos('LS1', 'Trackbar_1')
    LV1 = cv2.getTrackbarPos('LV1', 'Trackbar_1')
    UH1 = cv2.getTrackbarPos('UH1', 'Trackbar_1')
    US1 = cv2.getTrackbarPos('US1', 'Trackbar_1')
    UV1 = cv2.getTrackbarPos('UV1', 'Trackbar_1')

    LH2 = cv2.getTrackbarPos('LH2', 'Trackbar_2')
    LS2 = cv2.getTrackbarPos('LS2', 'Trackbar_2')
    LV2 = cv2.getTrackbarPos('LV2', 'Trackbar_2')
    UH2 = cv2.getTrackbarPos('UH2', 'Trackbar_2')
    US2 = cv2.getTrackbarPos('US2', 'Trackbar_2')
    UV2 = cv2.getTrackbarPos('UV2', 'Trackbar_2')

    LF1 = np.array([LH1, LS1, LV1], np.uint8)
    UF1 = np.array([UH1, US1, UV1], np.uint8)

    LF2 = np.array([LH2, LS2, LV2], np.uint8)
    UF2 = np.array([UH2, US2, UV2], np.uint8)

    maskHSV1 = cv2.inRange(frameHSV, LF1, UF1)
    maskHSV2 = cv2.inRange(frameHSV, LF2, UF2)
    maskHSV = cv2.add(maskHSV1, maskHSV2)

    #maskHSV = maskHSV1

    Result = cv2.bitwise_and(img, img, mask = maskHSV)

    cv2.imshow('Maimy Mask', maskHSV)
    cv2.imshow('Maimy Result', Result)

    if cv2.waitKey(50) & 0xFF == ord('s'):
        break

print(maskHSV)
print(maskHSV1)
print(maskHSV2)

cv2.destroyAllWindows()
