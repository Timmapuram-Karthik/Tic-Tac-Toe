# Tic Tac Toe

This is a simple command-line implementation of the Tic Tac Toe game in Python. It allows two players to take turns entering their moves and determines the winner based on the standard Tic Tac Toe rules.

## How to Play

1. Run the `Tic_Tac_Toe.py` file to start the game.

2. The first player is prompted to choose between 'X' and 'O'. Enter your choice and press Enter.

3. The game board is displayed, showing the numbers corresponding to each cell. The player needs to enter the number of the cell they want to mark.

4. Players take turns entering their moves until there is a winner or a draw.

5. If a player wins, the program displays a message indicating the winner. If it's a draw, the program displays a draw message.

6. The game ends, and you can choose to play again by running the script again.

## Example

Here's an example of how the game looks during play:

```
Player 1, choose X or O: X
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

X's turn
Enter the number to choose: 5
 1 | 2 | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9

O's turn
Enter the number to choose: 2
 1 | O | 3
-----------
 4 | X | 6
-----------
 7 | 8 | 9

...

X's turn
Enter the number to choose: 1
 X | O | O
-----------
 X | X | 6
-----------
 O | X | 9

X won!
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs.
