import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


class Motor():
    def __init__(self, EnaA, In1A, In2A, EnbB, In1B, In2B):
        self.EnaA = EnaA
        self.In1A = In1A
        self.In2A = In2A
        self.EnbB = EnbB
        self.In1B = In1B
        self.In2B = In2B
        GPIO.setup(self.EnaA, GPIO.OUT)
        GPIO.setup(self.In1A, GPIO.OUT)
        GPIO.setup(self.In2A, GPIO.OUT)
        GPIO.setup(self.EnbB, GPIO.OUT)
        GPIO.setup(self.In1B, GPIO.OUT)
        GPIO.setup(self.In2B, GPIO.OUT)
        self.pwmA = GPIO.PWM(self.EnaA, 50)
        self.pwmA.start(0)
        self.pwmB = GPIO.PWM(self.EnbB, 50)
        self.pwmB.start(0)

    def move(self, speed=0.5, turn=0, t=0):
        speed *= 20
        turn *= 7
        leftSpeed = speed - (turn)
        rightSpeed = speed + (turn)
        if leftSpeed > 27:
            leftSpeed = 27
        elif leftSpeed < -27:
            leftSpeed = -27
        if rightSpeed > 27:
            rightSpeed = 27
        elif rightSpeed < -27:
            rightSpeed = -27

        # print('leftSpeed', leftSpeed)
        # print('rightSpeed', rightSpeed)

        self.pwmA.ChangeDutyCycle(abs(leftSpeed))
        self.pwmB.ChangeDutyCycle(abs(rightSpeed))

        if leftSpeed > 0:
            GPIO.output(self.In1A, GPIO.HIGH)
            GPIO.output(self.In2A, GPIO.LOW)
        else:
            GPIO.output(self.In1A, GPIO.LOW)
            GPIO.output(self.In2A, GPIO.HIGH)

        if rightSpeed > 0:
            GPIO.output(self.In1B, GPIO.HIGH)
            GPIO.output(self.In2B, GPIO.LOW)
        else:
            GPIO.output(self.In1B, GPIO.LOW)
            GPIO.output(self.In2B, GPIO.HIGH)

        sleep(t)

    def stop(self, t=0):
        self.pwmA.ChangeDutyCycle(0)
        self.pwmB.ChangeDutyCycle(0)


def main():
    motor.move(.5, 0, 1)
    motor.stop(10)
    # motor.move(-0.05, 0, 1)
    # motor.stop(10)


if __name__ == "__main__":
    motor = Motor(2, 3, 4, 17, 22, 27)

    while True:

        main()

# Ena=2
# In1=3
# In2=4
# GPIO.setup(Ena,GPIO.OUT)
# GPIO.setup(In1.GPIO.OUT)
# GPIO.setup(IN2,GPIO.OUT)
# pwmA=GPIO.PWM(Ena,100)
# pwmA.start(0)

# pwmA.changeDutyCycle(60)
