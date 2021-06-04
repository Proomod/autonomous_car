import cv2
import numpy as np

cap = cv2.VideoCapture(0)


def piCam(display=False, size=[480, 240]):

    ret, frame = cap.read()

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # img = frame[int(frame.shape[0] / 2):, :, :]
    # img = cv2.resize(frame, (size[0], size[1]))
    if display:
        cv2.imshow('video', frame)

    return frame


if __name__ == "__main__":
    while True:
        piCam(display=True)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()