
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
