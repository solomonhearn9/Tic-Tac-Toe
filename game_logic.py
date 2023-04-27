# game_logic.py

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]


def is_valid_move(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '


def make_move(board, row, col, symbol):
    if is_valid_move(board, row, col):
        board[row][col] = symbol
        return True
    return False


def check_row_win(board, row):
    return board[row][0] == board[row][1] == board[row][2] != ' '


def check_col_win(board, col):
    return board[0][col] == board[1][col] == board[2][col] != ' '


def check_diag_win(board):
    return (board[0][0] == board[1][1] == board[2][2] != ' ') or (board[0][2] == board[1][1] == board[2][0] != ' ')


def check_full_board(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True


def check_game_over(board):
    for row in range(3):
        if check_row_win(board, row):
            return True, board[row][0]

    for col in range(3):
        if check_col_win(board, col):
            return True, board[0][col]

    if check_diag_win(board):
        return True, board[1][1]

    if check_full_board(board):
        return True, None

    return False, None
