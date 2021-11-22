from random import randint

class RunGame:
    '''
    Class runs the game sequence

    Attributes:
        p1 (Player) - first player object
        p2 (Player) - second player object
        gamestate (Board) - board object that is instantiated with random dimensions
    '''
    def __init__(self, player1, player2):
        """
        Checks the location of a player on the grid and responds accordingly
        Args: 
            p1 (Player) - first player object
            p2 (Player) - second player object
        Side effects:
            Sets self.gamestate to a new Board object with random dimensions
        """
        self.p1 = player2
        self.p2 = player2
        self.gamestate = self.createRandomStartState(self.p1, self.p2)
    
    def createRandomStartState(self, player1, player2):
        """
        Create new random board object
        Args: 
            p1 (Player) - first player object
            p2 (Player) - second player object
        Returns:
            board (Board) - a new Board object with random dimensions
        """
        dim = randint(8, 15)
        return Board(dim, player1, player2)

    
    def runGame(self):
        '''
        Runs the game loop sequence.

        Side Effects:
            Runs game, changes the players' positions in the game state, runs until game is over.
        '''

        # Starting with player 1
        currentPlayer = self.p1

        # Run game til 
        while not self.gameEnded():
            
            playerActions = self.gamestate.getActions(currentPlayer)
            action = input(f"Choose an move: {playerActions}")
            while not action in playerActions:
                action = input(f"Choose an move: {[a for a in playerActions]}")
        
            self.gamestate.turn(currentPlayer, action)
            
            self.gamestate.displayScores()

            if currentPlayer == self.p1:
                currentPlayer = self.p2
            else:
                currentPlayer = self.p1

    def gameEnded(self):
        '''
        Decides when the game is over

        Returns:
            winner (Player, None) - The winning player of the game, None if no winner
        
        '''
        if self.gameState.p1.score == 10 or self.gameState.p2.score == 10:
            sc = {self.gameState.p1:self.gameState.p1.score, self.gameState.p2:self.gameState.p2.score}
            return max(sc, key = lambda x: sc[x])
        elif self.gameState.player1.health <= 0 or self.gameState.player2.health <= 0:
            sc = {self.gameState.p1:self.gameState.p1.health, self.gameState.p2:self.gameState.p2.health}
            return max(sc, key = lambda x: sc[x])
        return None
    

    




    

    






