from numpy import disp
#from joystickModule import joyStick
from MotorModule import Motor
import keyPressModule as keyInput
from lanedetectionModule import getLaneCurve, initilaizePoints
from cameraModule import piCam
import cv2
#import joystickModule as joys

motor = Motor(2, 3, 4, 17, 22, 27)

runCamera = False
joyStick = False

# keyInput.init()

# if runCamera: piCam()


def main():
    img = piCam(display=True)
    curveVal = getLaneCurve(img, display=2)
    print(curveVal)
    sen = 0.89
    maxVal = 0.3
    if curveVal > maxVal: curveVal = maxVal
    if curveVal < -maxVal: curveVal = -maxVal

    if (curveVal > 0):
        sen = 0.8
        if curveVal < 0.05: curveVal = 0
    else:
        if curveVal < 0.08: curveVal = 0

    motor.move(-0.20, -curveVal * sen, 0.1)
    cv2.waitKey(1)


if __name__ == "__main__":
    initilaizePoints()
    while 1:
        main()
        # if joyStick:
        #     jsVal = joys.joyStick()
        #     print(jsVal)
        #     motor.move(jsVal['axis2'], jsVal['axis1'], 0.1)

        # # else:
        # #     if keyInput.keyPressed('w'):
        # #         print("w pressed")
        # #         motor.move(-0.1, 0, 0.1)
        # #     elif keyInput.keyPressed('s'):
        # #         print('s pressed')
        # #         motor.move(0.1, 0, 0.1)

        # #     elif keyInput.keyPressed('a'):
        # #         print('A pressed')
        # #         motor.move(-0.1, -0.2, 0.1)
        # #     elif keyInput.keyPressed('d'):
        # #         print('d pressed')
        # #         motor.move(-0.1, 0.2, 0.1)
        # else:
        #     motor.stop()
