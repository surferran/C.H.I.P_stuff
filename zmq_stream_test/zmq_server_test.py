"""
from https://stackoverflow.com/questions/43817161/how-to-send-opencv-video-footage-over-zeromq-sockets 
"""
import zmq

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://*:5555')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, '')

while True:
    try:
        frame = footage_socket.recv_string()
        print ("{0:}".format( frame if len( frame ) > 0 else "." ))
    except KeyboardInterrupt:
        break        

print ("\n\nBye bye\n")