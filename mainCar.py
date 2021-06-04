import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cameraModule as cM
import MotorModule as mM

# model = load_model(
#     '/home/pi/autonomouscar/DataCollected/lane_navigation_check.h5')
#Load the TFLite model and allocate tensors.
interpreter = tf.lite.Interpreter(
    model_path="/home/pi/autonomouscar/DataCollected/lanenavigatonlite-2.tflite"
)
interpreter.allocate_tensors()

# # Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# # Test the model on random input data.
# input_shape = input_details[0]['shape']

# interpreter.set_tensor(input_details[0]['index'], input_data)

# interpreter.invoke()

# # The function `get_tensor()` returns a copy of the tensor data.
# # Use `tensor()` in order to get a pointer to the tensor.
# output_data = interpreter.get_tensor(output_details[0]['index'])
# print(output_data)
steeringSen = 0.9  # Steering Sensitivitys
maxThrottle = 0.25  # Forward Speed %
motor = mM.Motor(2, 3, 4, 17, 22, 27)  # Pin Numbers


######################################
def img_preprocess(image):
    height, _, _ = image.shape
    image = image[int(height / 2):, :, :]
    # # remove top half of the image, as it is not relevant for lane following
    # image = change_brightness(image, value=30)

    image = cv2.cvtColor(
        image, cv2.COLOR_BGR2YUV
    )  # Nvidia model said it is best to use YUV color space
    image = cv2.GaussianBlur(image, (3, 3), 0)
    image = cv2.resize(image,
                       (200, 66))  # input image size (200,66) Nvidia model
    image = image / 255  # normalizing
    return image


def change_brightness(img, value=30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2RGB)
    return img


while True:
    img = cM.piCam(True, size=[240, 120])
    img = np.asarray(img)
    img = img_preprocess(img)
    img = np.array([img])
    input_data = np.array(img, dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    # steering = float(model.predict(img))
    steering = interpreter.get_tensor(output_details[0]['index'])
    print(steering * steeringSen)
    motor.move(maxThrottle, steering * steeringSen)
    cv2.waitKey(1)
