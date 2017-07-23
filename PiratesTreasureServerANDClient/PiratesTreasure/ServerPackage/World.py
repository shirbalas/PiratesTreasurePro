import random
from PiratesTreasure.ServerPackage import Cell
from PiratesTreasure.ServerPackage import Player

class World:
    def __init__(self,players = []):
        self.M_rows = 10
        self.N_columns = (10 + len(players))
        #self.listOfPlayersOnBoard = self.makeListOfPlayersOnTheBoard(players)
        self.CreateWorld(self.M_rows, self.N_columns)

    def MovePlayer(self,Player_id,NewI,NewJ,players = []):
        for c in players:
            if (players[c].PlayerID == Player_id):
                players[c].i = NewI
                players[c].j = NewJ


    """""
    def makeListOfPlayersOnTheBoard(self,players):
        listPlayers = []
        for c in players:
            listPlayers[c].append(PlayersOnTheBoard(c))  # i add a list of players on the board to know their location
        return listPlayers
    """

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

