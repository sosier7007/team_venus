import random

class Player:
    """An object representing one player in the game
    
    Attributes:
    - hp (int) - the number of health points that a player has
    - loot (int) - the amount of treasure that a player has
    - location (str) - the current location of the player
    
    """
    def __init__(self, hp, col, row, loot = 0):
        self.hp = hp 
        self.loot = loot
        self.col = col
        self.row = row

    def turn(row, col):
        """Allows the player to take a turn
        
            Arguments:
            - row (int) - the current row that the player is in
            - row (int) - the current row that the player is in
        
            Returns:
            - (row, col) (tuple) - the new coordinates of the player
        
            """
        steps = random.randint(1,6)
        direction = ["left", "right", "up", "down"]
        turn_direction = random.choice(direction)
        if turn_direction == "left":
            col -= steps
        elif turn_direction == "right":
            col += steps
        elif turn_direction == "up":
            row += steps
        elif turn_direction == "down":
            row -= steps

        if col <= 0:
            col = 0
        
        if col >= 9:
            col = 9

        if row <= 0:
            row = 0
        
        if row >= 9:
            row = 9

        return (row, col)

