"""""
import socket
import math
import sys
import random
import json
import requests
import self as self


server_socket = socket.socket()

server_socket.bind(("0.0.0.0", 6457))

server_socket.listen(5)
while(1):
    (client_socket, client_address) = server_socket.accept()
    client_name = client_socket.recv(1024)
    toclient = "Hello" + " " + client_name.decode("utf-8")
    client_socket.send(bytes(toclient ,"utf-8"))

client_socket.close()#closeing the connect between the client and the server
server_socket.close()#closeingthe socket of the server

globIDPlayer = 0
globIDRoom = 0
"""
"""""
GlobRoomsList = []
###### manageGlobRoomsList #########
class manageGlobRoomsList:
    def __init__(self):
        None    # do nothing

    def AddRoomToListOfRooms(self):
        global GlobRoomsList
        GlobRoomsList.append(self)

    def ListOfRooms(self):
        global GlobRoomsList
        return GlobRoomsList

    def GetRoom(self,numRoom):
        global GlobRoomsList
        return GlobRoomsList[numRoom]

    def joinExsistRoom_0(self,numRoom,C_socket):
        global GlobRoomsList
        GlobRoomsList[numRoom].AddPlayerToTheRoom(C_socket)  # i created and added player to the roon he ask for

"""
"""""
####### player ########
class Player:
    def __init__(self,i,j):
        global globIDPlayer
        self.PlayerID = self.increaseglobIDPlayer()
        self.ShipTreasureCoins = 0
        self.Location_i = i
        self.Location_j = j

    def increaseglobIDPlayer(self):
        global globIDPlayer
        globIDPlayer +=1

    #def AddCoins(self):

########### Room ##########
class Room:
    def __init__(self):
        global globIDRoom
        self.RoomID = self.increaseglobIDRoom()
        self.players = []
        self.isstart = False
        manageGlobRoomsList().AddRoomToListOfRooms(self)   #add the new room to the list of rooms

        #self.newWorld = World(self.players)

    def increaseglobIDRoom(self):
        global globIDRoom
        globIDRoom +=1

    def AddPlayerToTheRoom(self,C_socket):
        p = Player.__init__(0,0)    #make new player , at the bigining i and j are 0
        self.players.append(p)   #add this player to the list of players in the room
        if (len(self.players) == 5):
            Game().StartGame(C_socket)
            self.worldMaker()
        else:
            Game().DontStartTheGameYet(C_socket)


    def worldMaker(self):
        global GlobRoomsList
        if(len(self.players) == 5):    # this line isnt nassary because i chack earlier
            self.newWorld = World(manageGlobRoomsList.GetRoom(self.RoomID).players)  #when i have 5 player in the room i make the world


####### World ######
class World:
    def __init__(self,players = []):
        self.M_rows = 10
        self.N_columns = (10 + len(players))
        #self.listOfPlayersOnBoard = self.makeListOfPlayersOnTheBoard(players)
        self.CreateWorld(self.M_rows, self.N_columns)

    def makeListOfPlayersOnTheBoard(self,players):
        listPlayers = []
        for c in players:
            listPlayers[c].append(PlayersOnTheBoard(c))  # i add a list of players on the board to know their location
        return listPlayers

    def CreateWorld(self,rows,column):
        cell_board = []
        for y in range(rows):
            cell_board.append([])
        self.FillBoard(cell_board, rows, column)


    def FillBoard(self,cell_board,rows,columns):
        #islandORsea = random.randint(0,1)   #Determines whether its sea or island
        for y in range(rows):
            for x in range(columns):
                cell_board[y][x] =   Cell(0)               #filled the board in sea                                                      #self.CellState(islandORsea) #Determines the numbers of Gold coins in each cell

            while ((rows * columns) / 3):
                cell_board[random.randint(rows,columns)][random.randint(rows,columns)] = Cell(1)    #One-third of the Board is island



####### Cell ######
class Cell:
    def __init__(self,state):
        self.CoinsNumber = self.CellState(state)
        self.seaorland = state

    def GetCoinsNumber(self):
        return self.CoinsNumber

    def SetCoinsNumber(self,newnumofcoins):
        self.CoinsNumber = newnumofcoins

    def CellState(self, state):
        if state == 1:  # island
            return (random.randint(1, 10))  # TreasureBox = (between 1 to 10)
        elif state == 0:  # sea
            return 0  # TreasureBox = 0

######## PlayersOnTheBoard #######
class PlayersOnTheBoard:
    def __init__(self,playerId,i,j):
        self.IdOfPlayer = playerId

"""
"""""
class Server:
    def __init__(self):
        self.server_socket = socket.socket()

    def ConnectionToClient(self):
        self.bind(("127.0.0.1", 9876))
        self.listen(5)

    def getInfoFromTheClient(self):
            (client_socket, client_address) = self.accept()
            client_data = client_socket.recv(1024)  #recv the data
            client_data = int(client_data.decode("utf-8"))  # get in string and i need in int so i did casting  #decode
            #self.clientChoice = toclient  # the number the sclient choose
            return [client_data, client_socket]

    def CloseTheSocket(self,C_socket):
        C_socket.close()  # closeing the connect between the client and the server
        self.server_socket.close()  # closeingthe socket of the server


class Game:
    def __init__(self):
        None

    def StartGame(self,C_socket):
        C_socket.send(bytes("THE GAME START!", "utf-8"))

    def DontStartTheGameYet(self,C_socket):
        C_socket.send(bytes("there are ander 5 players in the room", "utf-8"))
"""
""""
def main():
    SerSOCK = Server()
    SerSOCK.ConnectionToClient()
    while True:
        try:
            DataOfTheClient , socketOFclient = SerSOCK.getInfoFromTheClient()
            data = json.loads(DataOfTheClient)
            op = data.get("NumberOfOption")  #i get the option number
            if op == 0:
                manageGlobRoomsList().joinExsistRoom_0(DataOfTheClient.get("NumOfExistentRoom"),socketOFclient)
            elif op == 1:
                manageGlobRoomsList().ListOfRooms()
            elif op == 2:
                Room()
        except ValueError:
            socketOFclient.send(bytes(300, "utf-8"))
            continue

    SerSOCK.CloseTheSocket(socketOFclient)


        #manageGlobRoomsList().options(client_status,)

    main()
"""
