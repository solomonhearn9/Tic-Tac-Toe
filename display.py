# display.py

import os


import os
import platform

def clear_screen():
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")



def print_instructions():
    print("\nInstructions:")
    print("Enter the row and column of the cell you want to mark.")
    print("Rows and columns are numbered 1, 2, or 3.")
    print("Separate the row and column with a space.")
    print("\nExample: 1 3 (This will mark the first row and third column)\n")


def print_board(board):
    print("  1 2 3")
    for i, row in enumerate(board, start=1):
        print(i, end=' ')
        for cell in row:
            print(cell, end='|')
        print("\b ")  # Remove the trailing vertical bar and add a space
        if i < 3:
            print("  -+-+-")
