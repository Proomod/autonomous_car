import pandas as pd
import os
import cv2
from datetime import datetime

global imgList, steeringList
countFolder = 0
count = 0
imgList = []
steeringList = []

dataDirectory = os.path.join(os.getcwd(), "DataCollected")

while os.path.exists(os.path.join(dataDirectory, f"IMG{str(countFolder)}")):
    countFolder += 1
newPath = dataDirectory + "/IMG" + str(countFolder)
os.makedirs(newPath)


def saveData(img, steering):
    now = datetime.now()
    timestamp = str(datetime.timestamp(now)).replace(".", "")
    fileName = os.path.join(newPath, f"Image_{timestamp}.jpg")
    cv2.imwrite(fileName, img)
    imgList.append(fileName)
    steeringList.append(steering)


def saveLog():
    # global imgList, steeringList
    rawData = {
        "Image": imgList,
        "Steering": steeringList,
    }
    df = pd.DataFrame(rawData)
    df.to_csv(
        os.path.join(dataDirectory, f"log_{str(countFolder)}.csv"),
        index=False,
        header=False,
    )
    print("Log saved")
    print("Total images:", len(imgList))


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    for x in range(10):
        success, img = cap.read()
        saveData(img, 0.5)
        cv2.waitKey(1)
        cv2.imshow("ImAGE", img)

    saveLog()