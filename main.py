# main.py

import os
import sys
from game_logic import check_game_over, make_move, initialize_board
from display import print_board, print_instructions, clear_screen
from player import Player
from computer import Computer


def get_player_names():
    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name or 'CPU' to play against the computer: ")
    return player1_name, player2_name


def choose_difficulty():
    difficulty = input("Choose the computer's difficulty level (easy, medium, hard): ").lower()
    while difficulty not in ['easy', 'medium', 'hard']:
        print("Invalid input. Please enter 'easy', 'medium', or 'hard'.")
        difficulty = input("Choose the computer's difficulty level (easy, medium, hard): ").lower()
    return difficulty

def get_user_move(board, current_player):
    while True:
        try:
            row, col = map(int, input(f"{current_player.name}, enter your move (row col): ").split())
            if make_move(board, row - 1, col - 1, current_player.symbol):
                break
            else:
                print("Invalid move. Please enter a valid row and column.")
        except ValueError:
            print("Invalid input. Please enter a valid row and column.")
        except IndexError:
            print("Invalid input. Please enter a valid row and column.")
    return row - 1, col - 1

def play_game(board, player1, player2):
    current_player = player1
    while True:
        clear_screen()
        print_board(board)
        print_instructions()

        if isinstance(current_player, Computer):
            row, col = current_player.make_move(board)
            make_move(board, row, col, current_player.symbol)
        else:
            row, col = get_user_move(board, current_player)

        game_over, winner_symbol = check_game_over(board)
        if game_over:
            clear_screen()
            print_board(board)
            if winner_symbol is None:
                print("It's a draw!")
            else:
                print(f"{current_player.name} wins!")
                current_player.total_wins += 1
            break

        current_player = player2 if current_player == player1 else player1


def main():
    clear_screen()
    print("Welcome to Tic-Tac-Toe!")

    player1_name, player2_name = get_player_names()
    player1 = Player(player1_name, 'X')
    if player2_name.upper() == 'CPU':
        difficulty = choose_difficulty()
        player2 = Computer('CPU', 'O', difficulty)
    else:
        player2 = Player(player2_name, 'O')

    board = initialize_board()

    play_game(board, player1, player2)


if __name__ == "__main__":
    main()
