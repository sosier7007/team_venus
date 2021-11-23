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
    '''
    Class runs the game 

    Attributes:
    player1(): first player
    player2(): second player
    
    '''
    def __init__(self, player1, player2):
        self.gamestate = self.createRandomStartState(player1, player2)

    
    def runGame(self):
        '''
        Runs the game

        Args:
        player1(): player1 object
        player2(): player2 object
        '''

        # Starting with player 1
        currentPlayer = self.player1

        # Run game til 
        while not self.gameEnded():
            
            playerActions = self.gamestate.move_player(currentPlayer)
            action = input(f"Choose an move: {playerActions}")
            while not action in playerActions:
                action = input(f"Choose an move: {[a for a in playerActions]}")
        
            self.gamestate.move_player(currentPlayer, action)
            
            print(player1.loot, player1.hp)

            if currentPlayer == self.player1:
                currentPlayer = self.player2
            else:
                currentPlayer = self.player1

    def gameEnded(self):
        '''
        Decides when the game is over

        Side effects:
            Returns the winning player if health is 10 or if hp is gone or 
            returns none where the game has not ended
        
        '''
        if (self.gameState.player_1_score + self.gameState.player_1_score == 10):
            sc = {self.gameState.player_1:self.gameState.player_1_score, self.gameState.player_2:self.gameState.player_2_score}
            return max(sc, key = lambda x: sc[x])
        elif self.gameState.player_1_health <= 0 or self.gameState.player_1_health <= 0:
            sc = {self.gameState.player_1:self.gameState.player_1_health, self.gameState.player_2:self.gameState.player_2_health}
            return max(sc, key = lambda x: sc[x])
        return None
    
        
        
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