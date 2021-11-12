import random

class Board:
    """ A class for the grid that the game will be played on.
    Attributes:
        size(int) - the length of a row for the square board
        board(lists of str) - lists of dot characters to be printed as a grid
        treasures(list of tuples) - a list of random tuples indicating the 
            coordinates of treasures on the board
        traps(list of tuples) - a list of random tuples indicating the 
            coordinates of traps on the board
    """
    def __init__(self, size):
        self.size = size
        self.board = []
        for x in range(self.size):
            self.board.append(["\u2022"] * self.size)
        self.treasures = [(random.randint(0,self.size - 1), 
                           random.randint(0,self.size - 1)) for a in range(10)]
        self.traps = [(random.randint(0,self.size - 1), 
                       random.randint(0,self.size - 1)) for a in range(10)]
        
        
    def print_board(self):
        """Prints the board as a grid"""
        for row in self.board:
            print(" ".join(row))
    
    def check_space(self, player):
        """Checks the location of a player on the grid and responds accordingly
        Args: 
            player(Player obj) - a Player
        Side effects:
            Changes player's hp and loot attributes
            Changes board attribute's coordinate characters
        """
        for x,y in self.treasures:
            if (x == player.col and y == player.row and 
                self.board[x][y] is "\u2022"):
                player.loot = player.loot + random.randint
                self.board[player.row][player.col] = "O"
        
        for x,y in self.traps:
            if (x == player.col and y == player.row and 
                self.board[x][y] is "\u2022"):
                player.hp = player.hp - random.randint
                self.board[player.row][player.col] = "X"

