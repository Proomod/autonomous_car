import cameraModule as wM
import dataCollectionModule as dcM
import joystickModule as jsM
import MotorModule as mM
import cv2
from time import sleep

maxThrottle = 0.2
motor = mM.Motor(2, 3, 4, 17, 22, 27)
record = 0

while True:

    joyVal = jsM.joyStick()

    steering = joyVal["axis1"]

    throttle = joyVal["o"] * maxThrottle
    if joyVal["share"] == 1:
        if record == 0: print("Recording Started...")
        record += 1
        sleep(0.300)
    if record == 1:
        img = wM.piCam(True, size=[240, 140])
        dcM.saveData(img, steering)
    elif record == 2:
        print("record saved")
        dcM.saveLog()
        record = 0
    motor.move(throttle, steering)
    cv2.waitKey(1)