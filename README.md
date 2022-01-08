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

  a. This function (find_move) finds the empty positions and places its marker in a random empty position. It's currently commented in my code. Only available in        'tictactoe_CLI.py' file, line 182.  
  
  b. This function (find_GoodMove) finds an empty position which might be beneficial in the next program's move and places its marker there. I would explain this function using an example.
  
  I would refer according to the following positions in this example. 'X' is the player's move and 'O' is the program's move.
  7 | 8 | 9
  ---------
  4 | 5 | 6
  ---------
  1 | 2 | 3
  
  Now, consider this scenario 1:
  7 | 8 | 9
  ---------
  4 | X | O
  ---------
  1 | 2 | 3
  
  The program will mark its position in one of the following positions: 9, 3. Because, it is considering the 'O' at position 6 to make 3 marks in a row in next few moves.
  
  Scenario 2:
  7 | 8 | 9
  ---------
  4 | O | X
  ---------
  1 | 2 | 3
  
  The program will mark its position in one of the following positions: 1, 2, 3, 7, 8, 9. Because, it is considering the 'O' at position 5 which increases the chances of putting   3 marks in a row i.e. vertically and diagonally.
  
  Scenario 3:
  7 | O | 9
  ---------
  O | X | X
  ---------
  1 | 2 | 3
  
  The program will mark its position in at 7 because it gives the program 2 opportunities of winning. If the player puts the marker at position 1, the program will simply win by   putting its marker at position 9. Similarly, if the player puts the marker at position 9 to block its path, the program will simply win by putting its marker at position 1.
  
  Hence, the third step of my algorithm finds the best chances of winning in the next move.
