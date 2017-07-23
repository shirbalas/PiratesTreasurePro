import socket
import json
import requests
import self as self

"""
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 6457))#ip of the localhost

    #nb = str(input('Choose a number: '))
    client_socket.send(bytes("shir","utf-8"))
    data = client_socket.recv(1024)
    print("The server sent: " + data)
    data = data.decode("utf-8")

    client_socket.close()

########## class Menu #########
class Menu():

    def __init__(self):
        None  #do nothing

    def displayMenu(self):
        print("to join to existent room input 0" + "\nto ask from the server the List of existing rooms input 1" + "\nto ask from the server to create(and join to the) new room input 2" +
            "\nto choose cell please input 3" +"\n")

    def displayResult(self,res):
        print(res)

########## class Session ############
class Session:

    def __init__(self):
        self.client1 = socket.socket()    #open socket


    def SocketsConnection(self):
        self.client1.connect(("127.0.0.1", 9876))   #open connection with the server

    def SocketCloser(self):
        self.client1.close()


"""
"""""
########### class UserChoice ###########
class UserChoice:

    def __init__(self):
        None  # do nothing

    def joinExistentRoom_0(self,connect):
        num_of_room = input("please enter number of room: ")
        data = "{NumOfExistentRoom:" +num_of_room+" , NumberOfOption: 0 }"   #0 Indicates to the server what the client meant to do
        data_json = json.dumps(data)
        connect.send(data_json, "utf-8")  #encode
        serverResponse = connect.recv(1024)
        serverResponse = serverResponse.decode("utf-8")  #decode
        print(serverResponse)
        
        
        if( serverResponse ==  300) :                    #300 is not-success
            print("ERROR : The room probably does not exist OR there are ander 5 players in the room")
        else:
            print("The game starts when you have 5 players in the room")  # The game starts when you have at least 5 players in the room

    def ToSeeTheListOfRooms_1(self,connect):
         data = "{NumberOfOption: 1 }"
         data_json = json.dumps(data)
         connect.send(data_json, "utf-8")  # encode
         serverResponse = connect.recv(1024)
         serverResponse = serverResponse.decode("utf-8")   #decode
         print("The lost of the rooms : " + serverResponse)


    def AskForCreateNewRoom_2(self,connect):
        data = "{NumberOfOption: 1 }"
        data_json = json.dumps(data)
        connect.send(data_json, "utf-8")  # encode



########## Main ##############
def main():

    S = Session()
    connect = S.SocketsConnection()
    m = Menu()
    m.displayMenu()
    while True:
        str = input("please enter number between 0 to 3")
        number = int(str) #casting from string to int
        U=UserChoice()
        if (number == 0):
            U.joinExistentRoom_0(connect)
        elif(number == 1):
            U.ToSeeTheListOfRooms_1(connect)
        elif (number == 2):
            U.AskForCreateNewRoom_2(connect)

    S.SocketCloser()


if __name__ == "__main__":
    main()
"""