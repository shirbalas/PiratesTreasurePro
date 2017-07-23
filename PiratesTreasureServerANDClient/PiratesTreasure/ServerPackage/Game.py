class Game:
    def __init__(self):
        None

    def StartGame(self,C_socket):
        C_socket.send(bytes("THE GAME START!", "utf-8"))

    def DontStartTheGameYet(self,C_socket):
        C_socket.send(bytes("there are ander 5 players in the room", "utf-8"))
