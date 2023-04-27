# computer.py

import random
from player import Player


class Computer(Player):
    def __init__(self, name, symbol, difficulty):
        super().__init__(name, symbol)
        self.difficulty = difficulty

    def make_move(self, board):
        if self.difficulty == 'easy':
            return self.random_move(board)
        elif self.difficulty == 'medium':
            return self.medium_move(board)
        else:
            return self.hard_move(board)

    def random_move(self, board):
        row, col = random.randint(0, 2), random.randint(0, 2)
        while not self.is_valid_move(board, row, col):
            row, col = random.randint(0, 2), random.randint(0, 2)
        return row, col

    def medium_move(self, board):
        for row in range(3):
            for col in range(3):
                if self.is_valid_move(board, row, col):
                    if self.can_win(board, row, col, self.symbol) or self.can_win(board, row, col, self.opponent_symbol()):
                        return row, col
        return self.random_move(board)

    def hard_move(self, board):
        # TODO: Implement a more advanced AI algorithm for the hard difficulty level
        return self.medium_move(board)

    def opponent_symbol(self):
        return 'X' if self.symbol == 'O' else 'O'

    def is_valid_move(self, board, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

    def can_win(self, board, row, col, symbol):
        board[row][col] = symbol
        game_over, winner_symbol = self.check_game_over(board)
        board[row][col] = ' '
        return winner_symbol == symbol

    def check_row_win(self, board, row):
        return board[row][0] == board[row][1] == board[row][2] != ' '

    def check_col_win(self, board, col):
        return board[0][col] == board[1][col] == board[2][col] != ' '

    def check_diag_win(self, board):
        return (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[0][2] == board[1][1] == board[2][0] != ' ')

    def check_full_board(self, board):
        for row in board:
            for cell in row:
                if cell == ' ':
                    return False
        return True

    def check_game_over(self, board):
        for row in range(3):
            if self.check_row_win(board, row):
                return True, board[row][0]

        for col in range(3):
            if self.check_col_win(board, col):
                return True, board[0][col]

        if self.check_diag_win(board):
            return True, board[1][1]

        if self.check_full_board(board):
            return True, None

        return False, None
