import sys
import json
#import requests

from PiratesTreasureClientSide.ClientPackage1 import Menu
from PiratesTreasureClientSide.ClientPackage1 import UserChoice
from PiratesTreasureClientSide.ClientPackage1.Session import Session


def main():
    S = Session()
    connect = S.SocketsConnection()
    m = Menu.Menu()
    m.displayMenu()
    while True:
        try:
            str = input("please enter number between 0 to 3")
            number = int(str) #casting from string to int
            U=UserChoice.UserChoice()
            if (number == 0):
                U.joinExistentRoom_0(connect)
            elif(number == 1):
                U.ToSeeTheListOfRooms_1(connect)
            elif (number == 2):
                U.AskForCreateNewRoom_2(connect)
             #elif (number == 4):       #its the option that the client choose a i and j
        finally:
            S.SocketCloser()




if __name__ == "__main__":
    main()
