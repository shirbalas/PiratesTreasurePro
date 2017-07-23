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

