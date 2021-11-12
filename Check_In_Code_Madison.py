import random

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

print(turn(1, 2))