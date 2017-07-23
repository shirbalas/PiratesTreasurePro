import json

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
        """""
        if( serverResponse ==  300) :                    #300 is not-success
            print("ERROR : The room probably does not exist OR there are ander 5 players in the room")
        else:
            print("The game starts when you have 5 players in the room")  # The game starts when you have at least 5 players in the room
        """

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

    #def

