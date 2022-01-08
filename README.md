# tic-tac-toe (Python)
There are 2 python files for tic tac toe:
tictactoe_CLI.py (to play in Command Line Interface) and tictactoe_GUI.py (to play in Graphical User Interface).
For tictactoe_CLI.py, numpad is suggested.
The pygame library is used in tictactoe_GUI.py.
There are 2 modes in this game:

1 player mode: Play with computer.

2 player mode: Play with human.

You can also play directly using the 'exe' file in the 'game' folder but make sure to download the whole 'game' folder. The 'exe' file was made using 'pyinstaller' library.

# Algorithm
1. The program checks if it can win using just one move. If it can, it places the 'O' at the favourable position and wins the game.
2. Else, it checks if the player can win using just one move. If the player can, the program places the 'O' at the favourable position and the game continues (given there is just one way the player can win).
3. Else, the program would place its marker according to the function that isn't commented. I designed 2 functions for this purpose:
  a. This function finds the empty positions and places its marker in a random empty position. It's currently commented in my code.
  b. This function finds an empty position which might be beneficial in the next program's move and places its marker there. I would explain this function using an example.
