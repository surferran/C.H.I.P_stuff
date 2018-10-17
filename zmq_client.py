"""
from https://stackoverflow.com/questions/43817161/how-to-send-opencv-video-footage-over-zeromq-sockets 
but final adjustment by:
https://github.com/CT83/SmoothStream/

"""

import cv2
import zmq
import base64

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')

camera = cv2.VideoCapture(0)  # init the camera

frame_num = 0

while True:
    try:
        (grabbed, frame) = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # resize the frame
        retval, buffer = cv2.imencode('.jpg', frame) #, CV_IMWRITE_JPEG_QUALITY = 90)
        tmp = base64.b64encode(buffer)
        footage_socket.send(tmp)
        frame_num += 1

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        print ("\n\nBye bye\n")
        break