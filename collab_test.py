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
                           random.randint(0,self.size - 1)) for a in range(20)]
        self.traps = [(random.randint(0,self.size - 1), 
                       random.randint(0,self.size - 1)) for a in range(20)]
        
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
        for x, y in self.treasures:
            if (x == player.row and y == player.col and 
                self.board[x][y] == "\u2022"):
                player.loot = player.loot + random.randint(0, 10)
                self.board[x][y] = "O"
                print("Treasure acquired!")
        
        for x, y in self.traps:     
            if (x == player.row and y == player.col and 
                self.board[x][y] == "\u2022"):
                player.hp = player.hp - random.randint(0, 10)
                self.board[x][y] = "X"
                print("Oh no! Trap found...")
          
            

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
        
        if self.col >= 8:
            col = 8

        if self.row <= 0:
            self.row = 0
        
        if self.row >= 8:
            self.row = 8


class Game:
    """
    """
    def __init__(self, board, player1, player2):
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
    game_board.print_board()
    
    #print game instructions 
    
    name1 = input("Player 1, please enter your name: \n")
    print(f"Hello {name1}!")
    player1 = Player(name1)
    
    name2 = input("Player 2, please enter your name: \n")
    print(f"Hello {name2}!")
    player2 = Player(name2)
    
    #print player location on board
    #print loot and hp
    
    #game turn
    #check if game is over 
    #repeat
    
    player1.move_player()
    print(f"{player1.player_name} moved to space {player1.row}, {player1.col}")
    game_board.check_space(player1)
    game_board.print_board()
    
    player1.move_player()
    print(f"{player1.player_name} moved to space {player1.row}, {player1.col}")
    game_board.check_space(player1)
    game_board.print_board()
    print(player1.loot)
    print(player1.hp)
    print(game_board.treasures)
    print(game_board.traps)