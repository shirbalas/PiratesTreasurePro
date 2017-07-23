import socket
import sys
from threading import Thread
from time import sleep


class Session:
    def __init__(self):
        self.client1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # open socket

    def SocketsConnection(self):
        try:
            self.client1.connect(("127.0.0.1", 10000))  # open connection with the server
        except socket.error  as e:
            print("Error creating socket: %s" % e)
            sys.exit(1)


    def SocketCloser(self):
        self.client1.close()
