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
        """Prints the board for the game
        Side effects:
            prints the board that the game is taking place on, along
            with the positions of each player on the board
        """
        player_board = [r[:] for r in self.board]
        row1 = self.p1.row
        col1 = self.p1.col
        row2 = self.p2.row
        col2 = self.p2.col
        player_board[row1][col1] = "\u263A" 
        player_board[row2][col2] = "\u263B"
        for row in player_board:
            print(" ".join(row))
    
    def delete_p(self, player_name):
        """Prevents the player icons from appearing multiple times
        Args:
            player_name(str) - the name of the player
        Side effects:
            Removes a player's icon from their previous location
        """
        if player_name == self.p1.player_name:
            player = self.p1
        else:
            player = self.p2
        
        for x, y in self.treasures:
            if (x == player.row and y == player.col):
                self.board[x][y] = "\u25C7"
                break
            else:
                self.board[player.row][player.col] = "\u25E6"
        
        for x, y in self.traps:
            if ((x == player.row and y == player.col) and 
                self.board[x][y] == "\u25E6") :
                self.board[x][y] = "x"
    
    def check_space(self, player_name): 
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
            
        modifier = random.randint(1, 5)

        for x, y in self.treasures:
            if (x == player.row and y == player.col and 
                self.board[x][y] == "\u2022"):
                player.loot = player.loot + modifier
                self.board[x][y] = "O"
                print(f"\n{player.player_name} found {modifier} treasure!")
        
        for x, y in self.traps:     
            if (x == player.row and y == player.col and 
                self.board[x][y] == "\u2022"):
                player.hp = player.hp - modifier
                self.board[x][y] = "X"
                print(f"\nOh no! Trap found by {player.player_name}"
                      f"...they take {modifier} damage...")            
    
    def move_player(self, player_name, action, steps):
        """Determines which player should move
        Args:
            player_name(str) - the name of the player
            action(str) - the direction that the player will move in
            steps(int) - how many spaces the player will move
        Side effects:
            Changes the location of the player on the board
        """
        if player_name == self.p1.player_name:
            self.p1.move_player(action, steps, self.size)
        else:
            self.p2.move_player(action, steps, self.size)


class Player:
    """Creates one of the players for the game
    Attributes:
        player_name(str) - the name of the player
        loot(int) - how much treasure the player has
        hp(int) - how many health points a player has
        row(int) - the latitudal position of the player
        col(int) - the longitudal position of the player
    """
    def __init__(self, input):
        self.player_name = input 
        self.loot = 0
        self.hp = 10
        self.row = 0
        self.col = 0
        
    def move_player(self, turn_direction, steps, size): 
        """ Moves the player to a different space on the board
        Args:
            turn_direction (str) - the direction that the player wants to go in
            steps (int) - how many spaces the player will move
            size (int) - the dimensions of the board
        Side effects:
            Changes the value of 'rol' and 'col' for the player
        """
        
        if turn_direction == "left":
            self.col -= steps
        elif turn_direction == "right":
            self.col += steps
        elif turn_direction == "down":
            self.row += steps
        elif turn_direction == "up":
            self.row -= steps

        if self.col < 0:
            self.col = 0
        
        if self.col >= size:
            self.col = size - 1 

        if self.row < 0:
            self.row = 0
        
        if self.row >= size:
            self.row = size - 1


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
        """Creates a starting state for the board
        
        Args:
        - player1 (str) - the name of player 1
        - player2 (str) - the name of player 2
        
        Returns:
        - an instance of the Board class
        
        """
        # Return a new board with two new player objects created 
        # from the player name parameters
        return Board(Player(player1), Player(player2), size= 9)

    def runGame(self):
        '''
        Runs the game

        Args:
        player1(): player1 object
        player2(): player2 object
        '''

        # Start with player 1 - set currentPlayer to player 1's name
        currentPlayer = self.gamestate.p1.player_name

        # Run game until the game has ended
        while not self.gameEnded():
            
            print("")
            
            # Roll the dice, get a random number from 1-6
            roll = random.randint(1, 6)
            print(f"{currentPlayer} rolled a {roll}.")

            # List of player actions
            playerActions = ["left", "right", "up", "down"]

            # Ask user for a move
            action = input(f"Choose a move: {playerActions}")
            # Keep asking for a move until they input a valid one
            while not action in playerActions:
                print("Invalid move.")
                action = input(f"Choose a move: {[a for a in playerActions]}")
            
            self.gamestate.delete_p(currentPlayer)
                    
            # Move the current player in the chosen direction
            # for the number of steps rolled on the dice
            self.gamestate.move_player(currentPlayer, action, roll)

            # Check the current player's space, update their hp and loot
            self.gamestate.check_space(currentPlayer)

            # Display the board
            print('')
            self.gamestate.print_board()

            # Switch current player to the opposite player for the next turn
            if currentPlayer == self.gamestate.p1.player_name:
                currentPlayer = self.gamestate.p2.player_name
            else:
                currentPlayer = self.gamestate.p1.player_name
                print('')
                print(f"{self.gamestate.p1.player_name} has "
                      f"{self.gamestate.p1.loot} loot and "
                      f"{self.gamestate.p1.hp} health.")
                print(f"{self.gamestate.p2.player_name} has "
                      f"{self.gamestate.p2.loot} loot and "
                      f"{self.gamestate.p2.hp} health.")

    def gameEnded(self):
        '''
        Decides when the game is over

        Side effects:
            Returns the winning player if loot is 10 or if hp is gone or 
            returns none where the game has not ended
        
        '''
        # Check if either player has reached 10 loot
        if (self.gamestate.p1.loot >= 10 or self.gamestate.p2.loot >= 10):
            # Dictionary mapping player's name to their loot count
            sc = {
                self.gamestate.p1.player_name:self.gamestate.p1.loot, 
                self.gamestate.p2.player_name:self.gamestate.p2.loot, 
            }
            # Return the player with the higher loot
            return max(sc, key = lambda x: sc[x])

        # Check if either player has zero or less hp
        elif self.gamestate.p1.hp <= 0 or self.gamestate.p2.hp <= 0:
            # Dictionary mapping player's name to their hp count
            sc = {
                self.gamestate.p1.player_name:self.gamestate.p1.hp, 
                self.gamestate.p2.player_name:self.gamestate.p2.hp, 
            }
            # Return the player with the higher hp
            return max(sc, key = lambda x: sc[x])
        return None
    
        
if __name__ == "__main__":
    
    print('')
    print("Player 1 = \u263A")
    print("Player 2 = \u263B")
    print('')
    
    name1 = input("Player 1, please enter your name: \n")
    print(f"Hello {name1}!")
    print('')
    name2 = input("Player 2, please enter your name: \n")
    print(f"Hello {name2}!")

    g = Game(name1, name2)
    print('')
    g.gamestate.print_board()
    g.runGame()
    
    winner = g.gameEnded()
    print(f"\n Congratulations {winner} you win the game!")
    print('')
    
    