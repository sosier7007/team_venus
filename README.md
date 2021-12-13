# team_venus
INST 326 Collaborative Coding - Final Project
In this project, a two player game was created. In this game, two players compete in order to find treasure and avoid traps. There are two ways that the game can end:
1. One of the players collects 10 pieces of treasure.
2. One of the players loses all of their health points.

How To Run The Program
In order to run the program, simply type the needed Python command for your system (i.e. 'python3' or 'python'), followed by a space and then 'st.py'. This will begin the game.

How To Use The Program:
First, both players will be asked for their names. When prompted, simply type your desired name into the terminal and press either 'Enter' or 'Return' (depending on your computer). You will repeat this step for the second player.

After this, player 1 will be given a random number from 1-6 that represents how many spaces they can move (similar to rolling a six-sided dice). The player will then have the choice of which direction they want to move in, either up, down, right, or left. To choose your direction, type your direction into the terminal when prompted and press either 'Enter' or 'Return' (depending on your computer). After this, a new board will print with your updated position. For player 1, this position will be indicated by a black smiley face.

There are three potential outcomes when landing on a space.
1. You find some treasure, in which case your loot will increase. This is indicated by the statement 'Treasure Acquired!', which will be listed above the board. After you leave the space, it will be represented by a diamond.
2. You find a trap, which will cause your HP to decrease. This is indicated by the statement 'Oh no! Trap found...', which will be listed above the board. After you leave the space, it will be represented by an X.
3. You find an empty space, in which nothing will happen. After you leave the space, it will be represented by a black dot.

The same steps listed above will then occur for player 2. The only difference is that their position will be indicated by a white smiley face.

The game will alternate between both players until one of the game endings listed above occurs. After this, the game will print a statement saying who won, and the program will end.