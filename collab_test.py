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
    def __init__(self, player1, player2, size = 9):
        self.size = size
        self.board = []
        for x in range(self.size):
            self.board.append(["\u2022"] * self.size)
        self.treasures = [(random.randint(0,self.size - 1), 
                           random.randint(0,self.size - 1)) for a in range(20)]
        self.traps = [(random.randint(0,self.size - 1), 
                       random.randint(0,self.size - 1)) for a in range(20)]
        
        self.p1 = player1
        self.p2 = player2
        
    def print_board(self):
        """Prints the board as a grid"""
        for row in self.board:
            print(" ".join(row))
    
    def check_space(self, player_name): # make this into a function instead of a method
        """Checks the location of a player on the grid and responds accordingly
        Args: 
            player(Player obj) - a Player
        Side effects:
            Changes player's hp and loot attributes
            Changes board attribute's coordinate characters
        """

        if player_name == self.p1.player_name:
            player = self.p1
        else:
            player = self.p2


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
    
    def move_player(self, player_name, action, steps):
        if player_name == self.p1.player_name:
            self.p1.move_player(action, steps)
        else:
            self.p2.move_player(action, steps)
          
            

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
    
        
        
    def move_player(self, turn_direction, steps): 
        #change turn_direction to user input(rather than random)
        #print dice roll and instructions for player to see
        """
        """
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
            print("Bumped into a wall, stopping here.")
        
        if self.col >= 8:
            self.col = 8
            print("Bumped into a wall, stopping here.")

        if self.row <= 0:
            self.row = 0
            print("Bumped into a wall, stopping here.")
        
        if self.row >= 8:
            self.row = 8
            print("Bumped into a wall, stopping here.")


class Game:
    """
    Class runs the game 

    Attributes:
    player1(): first player
    player2(): second player
    """
    
    def __init__(self, player1, player2):
        self.gamestate = self.createRandomStartState(player1, player2)
    
    def createRandomStartState(self, player1, player2):
        return Board(Player(player1), Player(player2), size=random.randint(9, 15))

    
    def runGame(self):
        '''
        Runs the game

        Args:
        player1(): player1 object
        player2(): player2 object
        '''

        # Starting with player 1
        currentPlayer = self.gamestate.p1.player_name

        # Run game til 
        while not self.gameEnded():
            

            roll = random.randint(1, 6)
            print(f"You rolled a {roll}.")

            playerActions = ["left", "right", "up", "down"]

            action = input(f"Choose an move: {playerActions}")
            while not action in playerActions:
                print("Invalid move.")
                action = input(f"Choose an move: {[a for a in playerActions]}")
        

            self.gamestate.move_player(currentPlayer, action, roll)
            self.gamestate.check_space(currentPlayer)
            self.gamestate.print_board()


            

            if currentPlayer == self.gamestate.p1.player_name:
                currentPlayer = self.gamestate.p2.player_name
            else:
                currentPlayer = self.gamestate.p1.player_name

    def gameEnded(self):
        '''
        Decides when the game is over

        Side effects:
            Returns the winning player if loot is 10 or if hp is gone or 
            returns none where the game has not ended
        
        '''
        if (self.gamestate.p1.loot == 10 or self.gamestate.p2.loot == 10):
            sc = {
                self.gamestate.p1.player_name:self.gamestate.p1.loot, 
                self.gamestate.p2.player_name:self.gamestate.p2.loot, 
            }
            return max(sc, key = lambda x: sc[x])
        elif self.gamestate.p1.hp <= 0 or self.gamestate.p2.hp <= 0:
            sc = {
                self.gamestate.p1.player_name:self.gamestate.p1.hp, 
                self.gamestate.p2.player_name:self.gamestate.p2.hp, 
            }
            return max(sc, key = lambda x: sc[x])
        return None
    
        
        
if __name__ == "__main__":
    # # run game here
    # game_board = Board()
    # game_board.print_board()
    
    # #print game instructions 
    
    name1 = input("Player 1, please enter your name: \n")
    print(f"Hello {name1}!")
    
    name2 = input("Player 2, please enter your name: \n")
    print(f"Hello {name2}!")

    g = Game(name1, name2)
    g.runGame()
    
    # #print player location on board
    # #print loot and hp
    
    # #game turn
    # #check if game is over 
    # #repeat
    
    # # player1.move_player()
    # # print(f"{player1.player_name} moved to space {player1.row}, {player1.col}")
    # # game_board.check_space(player1)
    # # game_board.print_board()
    
    # # player1.move_player()
    # # print(f"{player1.player_name} moved to space {player1.row}, {player1.col}")
    # # game_board.check_space(player1)
    # # game_board.print_board()
    # # print(player1.loot)
    # # print(player1.hp)
    # # print(game_board.treasures)
    # # print(game_board.traps)

    