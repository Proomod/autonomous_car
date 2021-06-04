import cv2
import numpy as np


def thresholding(img):
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lowerWhite = np.array([58, 0, 0])
    upperWhite = np.array([179, 226, 255])
    maskWhite = cv2.inRange(imgHsv, lowerWhite, upperWhite)
    return maskWhite


def warpImg(img, points, w, h, inv=False):
    pts1 = np.float32(points)  # 4 points
    pts2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
    if inv:
        matrix = cv2.getPerspectiveTransform(pts2, pts1)
    else:
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imageWarp = cv2.warpPerspective(img, matrix, (w, h))
    return imageWarp


def getHistogram(img, minPer=0.2, display=True, region=1):
    if region == 1:

        histoVal = np.sum(img, axis=0)
    else:
        histoVal = np.sum(img[img.shape[0] // region:, :], axis=0)
    maxVal = np.max(histoVal)
    thresholdVal = minPer * maxVal
    indexArray = np.where(histoVal >= thresholdVal)
    # print(indexArray)
    basePoint = int(np.average(indexArray))

    if display:
        histoImg = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

        for x, intensity in enumerate(histoVal):

            cv2.line(
                histoImg,
                (x, img.shape[0]),
                (x, img.shape[0] - int(intensity // 255)),
                (255, 0, 255),
                1,
            )
            cv2.circle(histoImg, (basePoint, img.shape[0]), 20, (0, 200, 200),
                       cv2.FILLED)

        return basePoint, histoImg

    # print(imgHisto)
    return basePoint


def initializeTrackBars(initialTrackVals, wT=480, hT=240):
    cv2.namedWindow("Trackbars", cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", initialTrackVals[0], wT // 2,
                       empty)
    cv2.createTrackbar("Height Top", "Trackbars", initialTrackVals[1], hT,
                       empty)
    cv2.createTrackbar("Width Bottom", "Trackbars", initialTrackVals[2],
                       wT // 2, empty)
    cv2.createTrackbar("Height Bottom", "Trackbars", initialTrackVals[3], hT,
                       empty)


def empty():
    pass


def valTrackbars(wT=480, hT=240):
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    points = np.float32([
        (widthTop, heightTop),
        (wT - widthTop, heightTop),
        (widthBottom, heightBottom),
        (wT - widthBottom, heightBottom),
    ])
    print(points)

    return points


def drawPoints(img, points):
    for x in range(0, 4):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 16,
                   (0, 0, 200), cv2.FILLED)
    return img


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None,
                                                scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y],
                        (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                        None,
                        scale,
                        scale,
                    )
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y],
                                                  cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale,
                                         scale)
            else:
                imgArray[x] = cv2.resize(
                    imgArray[x],
                    (imgArray[0].shape[1], imgArray[0].shape[0]),
                    None,
                    scale,
                    scale,
                )
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver
