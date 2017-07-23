globIDPlayer = 0


class Player:
    def __init__(self, i, j):
        global globIDPlayer
        self.PlayerID = self.increaseglobIDPlayer()
        self.ShipTreasureCoins = 0
        self.Location_i = i
        self.Location_j = j

    def increaseglobIDPlayer(self):
        global globIDPlayer
        globIDPlayer += 1

        # def AddCoins(self):
