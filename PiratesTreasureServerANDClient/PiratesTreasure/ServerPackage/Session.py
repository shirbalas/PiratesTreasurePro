import socket
import sys
import self as self


class Session:

    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def ConnectionToClient_bind(self):
        try:
            self.server_socket.bind(("127.0.0.1",10000))
        except socket.gaierror as e:
            print("Error bind to the socket: %s" %e)
            self.CloseTheSocket(self)
            sys.exit(1)

    def ConnectionToClient_listen(self):
        self.server_socket.listen(10)

    #def ListenerToConnections(self):
    #    (client_socket, client_address) = self.accept()

    def getInfoFromTheClient(self):
            (client_socket, client_address) = self.accept()
            client_data = client_socket.recv(1024)  #recv the data
            client_data = int(client_data.decode("utf-8"))  # get in string and i need in int so i did casting  #decode
            #self.clientChoice = toclient  # the number the sclient choose
            return client_data, client_socket

    def CloseTheSocket(self,C_socket):
        C_socket.close()  # closeing the connect between the client and the server
        self.server_socket.close()  # closeingthe socket of the server
