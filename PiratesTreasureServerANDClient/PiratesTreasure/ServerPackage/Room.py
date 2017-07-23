from PiratesTreasure.ServerPackage import manageGlobRoomsList
from PiratesTreasure.ServerPackage import Player
from PiratesTreasure.ServerPackage import Game
from PiratesTreasure.ServerPackage import World


globIDRoom = 0
class Room:
    def __init__(self,C_socket):
        global globIDRoom
        self.RoomID = self.increaseglobIDRoom()
        self.players = []
        self.isstart = False
        manageGlobRoomsList().AddRoomToListOfRooms(self)   #add the new room to the list of rooms
        self.AddPlayerToTheRoom(C_socket)

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
