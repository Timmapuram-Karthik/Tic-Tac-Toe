class TicTacToe:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.player_1 = ""
        self.player_2 = ""
        self.current_player = ""

    def print_board(self):
        for row in self.board:
            print(" | ".join(map(str, row)))
            print("-" * 9)

    def choose_players(self):
        while True:
            player_1 = input("Player 1, choose X or O: ").upper()
            if player_1 == "X":
                self.player_1 = "X"
                self.player_2 = "O"
                break
            elif player_1 == "O":
                self.player_1 = "O"
                self.player_2 = "X"
                break
            else:
                print("Invalid input. Please choose X or O.")

    def make_move(self):
        while True:
            try:
                move = int(input("Enter the number to choose: "))
                if move < 1 or move > 9:
                    print("Invalid input. Choose a number between 1 and 9.")
                    continue
                row = (move - 1) // 3
                col = (move - 1) % 3
                if self.board[row][col] == "X" or self.board[row][col] == "O":
                    print("Invalid move. That position is already occupied.")
                    continue
                if self.current_player == self.player_1:
                    self.board[row][col] = self.player_1
                else:
                    self.board[row][col] = self.player_2
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2]:
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col]:
                return True

        # Check diagonals
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2]
            or self.board[0][2] == self.board[1][1] == self.board[2][0]
        ):
            return True

        return False

    def play_game(self):
        self.print_board()
        self.choose_players()
        self.current_player = self.player_1

        for _ in range(9):
            print(f"{self.current_player}'s turn")
            self.make_move()
            self.print_board()
            
            if self.check_winner():
                print(f"{self.current_player} won!")
                return

            if self.current_player == self.player_1:
                self.current_player = self.player_2
            else:
                self.current_player = self.player_1

        print("It's a draw!")

game = TicTacToe()
game.play_game()
