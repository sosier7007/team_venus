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
    def __init__(self, size = 9):
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
    
    def check_space(self, player): # make this into a function instead of a method
        """Checks the location of a player on the grid and responds accordingly
        Args: 
            player(Player obj) - a Player
        Side effects:
            Changes player's hp and loot attributes
            Changes board attribute's coordinate characters
        """
        for x,y in self.treasures:
            if (x == player.col and y == player.row and 
                self.board[y][x] is "\u2022"):
                player.loot = player.loot + random.randint(0, 10)
                self.board[player.row][player.col] = "O"
        
        for x,y in self.traps:
            if (x == player.col and y == player.row and 
                self.board[y][x] is "\u2022"):
                player.hp = player.hp - random.randint(0, 10)
                self.board[player.row][player.col] = "X"
                
    def change_space(self, row, col, char):
        """Manually change the character of a space on the board, for testing
        Args:
            row(int) - the row of desired coordinate
            col(int) - the column of desired coordinate
            char(str) - a symbol to replace the space with
        Side effects:
            Changes board attribute of Board
        """
        self.board[row][col] == char

#write a method or function that copies Board.board and changes player location to player icon + prints

class Player:
    """
    """
    def __init__(self, input):
        self.player_name = input 
        self.loot = 0
        self.hp = 10
        self.row = 0
        self.col = 0
        
    def move_player(self): 
        #change turn_direction to user input(rather than random)
        #print dice roll and instructions for player to see
        """
        """
        steps = random.randint(1,6)
        print
        direction = ["left", "right", "up", "down"]
        turn_direction = random.choice(direction)
        if turn_direction == "left":
            self.col -= steps
        elif turn_direction == "right":
            self.col += steps
        elif turn_direction == "up":
            self.row += steps
        elif turn_direction == "down":
            self.row -= steps

        if self.col <= 0:
            self.col = 0
        
        if self.col >= 9:
            col = 9

        if self.row <= 0:
            self.row = 0
        
        if self.row >= 9:
            self.row = 9


class Game:
    """
    """
    def __init__(self) -> None:
        pass
    
    def game_turn(self, board, player1, player2):
        pass
        #print board
        #players move
        #check spaces
        #print board again
        #print message
    
        
        
if __name__ == "__main__":
    # run game here
    game_board = Board()
    game_board.print_board
    
    #print game instructions for players
    
    name1 = input("Player 1, please enter your name: \n")
    print(f"Hello {name1}!/n")
    player1 = Player(name1)
    
    name2 = input("Player 2, please enter your name: \n")
    print(f"Hello {name2}!/n")
    player2 = Player(name2)
    
    #game turn
    #check if game is over 