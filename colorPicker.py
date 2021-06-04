import cv2
import numpy as np

# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(1)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)


def empty(a):
    pass


cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("Hue min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue max", "HSV", 179, 179, empty)
cv2.createTrackbar("SAT min", "HSV", 0, 255, empty)
cv2.createTrackbar("SAT max", "HSV", 255, 255, empty)
cv2.createTrackbar("VAL min", "HSV", 0, 255, empty)
cv2.createTrackbar("VAL max", "HSV", 255, 255, empty)

cap = cv2.VideoCapture(0)
frameCounter = 0
while True:
    frameCounter += 1
    if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        frameCounter = 0
    success, img = cap.read()
    if success:
        imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue min", "HSV")
    h_max = cv2.getTrackbarPos("Hue max", "HSV")
    s_min = cv2.getTrackbarPos("SAT min", "HSV")
    s_max = cv2.getTrackbarPos("SAT max", "HSV")
    v_min = cv2.getTrackbarPos("VAL min", "HSV")
    v_max = cv2.getTrackbarPos("VAL max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    hStack = np.hstack([img, mask, result])
    cv2.imshow("Horizotal Stacking", hStack)
    print(h_min, s_min, v_min, h_max, s_max, v_max)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()