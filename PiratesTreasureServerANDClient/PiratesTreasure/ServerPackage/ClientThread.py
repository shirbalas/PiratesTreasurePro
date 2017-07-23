from threading import Thread
import json
from PiratesTreasure.ServerPackage import ManageUserchoice
from time import sleep
from PiratesTreasure.ServerPackage import Session
import select

from PiratesTreasure.ServerPackage.ManageUserchoice import ManageUserChoice


class ClientThread(Thread):
    def __init__(self,client_socket):
        Thread.__init(self)
        self.clientSocket = client_socket

    def run(self):
        while True:
            daraClient = self.clientSocket.recv(1024)
            daraClient = daraClient.decode("utf-8")
            if (daraClient != ""):
                data = json.loads(daraClient)
                op = data.get("NumberOfOption")  #i get the option number
                numexsistroom = data.get("NumOfExistentRoom")  # i ger the Num Of Existent Room
                ManageUserChoice.diract_options(op,numexsistroom,self.clientSocket)
