from threading import Thread
from time import sleep
from PiratesTreasure.ServerPackage import Session
import select
from PiratesTreasure.ServerPackage import ClientThread

class ConnectionsThread(Thread):
    def __init__(self,val,sock):
        Thread.__init(self)
        self.val = val
        self.Sock = sock

    def run(self):
        while True:
            (client_socket, client_address) = self.Sock.accept()
            clientIsThread = ClientThread(client_socket)
            clientIsThread.start()










"""""
        TCP_IP = "127.0.0.1"
        TCP_PORT = 9876

        tcpServer = Session()
        tcpServer.ConnectionToClient_bind((TCP_IP, TCP_PORT))
        thread_listener =

        while True:
            print("Multithreaded Python server : Waiting for connections from TCP clients...")
            (conn, (ip, port)) = tcpServer.accept()
            newthread = ClientThread(ip, port)
            newthread.start()
            threads.append(newthread)

        for t in threads:
            t.join()
"""