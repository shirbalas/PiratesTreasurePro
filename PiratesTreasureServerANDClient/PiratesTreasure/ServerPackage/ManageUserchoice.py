import sys
import json
import requests
from PiratesTreasure.ServerPackage import Session
from PiratesTreasure.ServerPackage import manageGlobRoomsList
from PiratesTreasure.ServerPackage import Room
from PiratesTreasure.ServerPackage import ClientThread
from PiratesTreasure.ServerPackage import manageGlobRoomsList

class ManageUserChoice():
    def __init__(self):
        None

    def diract_options(option,numexsistroom,socketOFclient):

     try:
        # if (op == 4):
        if (option == 0):
            manageGlobRoomsList().joinExsistRoom_0(numexsistroom.get("NumOfExistentRoom"),socketOFclient)
        elif option == 1:
            manageGlobRoomsList().ListOfRooms()
        elif option == 2:
            Room(socketOFclient)
     except ValueError:
        socketOFclient.send(bytes(300, "utf-8"))
