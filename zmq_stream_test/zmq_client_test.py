"""
from https://stackoverflow.com/questions/43817161/how-to-send-opencv-video-footage-over-zeromq-sockets 
"""
import zmq

context = zmq.Context()
footage_socket = context.socket(zmq.PUB)
footage_socket.connect('tcp://localhost:5555')

counter = 0
while True:
    try:
        # FOR STREAMING, ALWAYS PREFER DESIGNS USING A NONBLOCKING MODE
        counter += 1
        footage_socket.send_string( str(counter) )               # PUB.send( SEQ ) -> *SUB*

    except KeyboardInterrupt:
        print ("\n\nBye bye\n")
        break
print(str(counter))
