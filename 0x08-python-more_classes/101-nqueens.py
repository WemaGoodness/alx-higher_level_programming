#!/usr/bin/python3

"""
Module Documentation:
This module defines a solution for the N-Queens problem using backtracking.
"""


import sys


def print_solution(board):
    """
    Function Documentation:
    Prints the N-Queens solution represented by the board.
    """
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i] == j:
                solution.append([i, j])
    print(solution)


def is_safe(board, row, col):
    """
    Function Documentation:
    Checks if placing a queen at the specified row and column is safe.
    """
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True


def solve_nqueens(board, col):
    """
    Function Documentation:
    Solves the N-Queens problem using backtracking.
    """
    n = len(board)
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col):
            board[col] = i
            solve_nqueens(board, col + 1)


def check_args():
    """
    Function Documentation:
    Checks command-line arguments and returns specified N for N-Queens problem
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def main():
    """
    Function Documentation:
    Main function to parse command-line arguments and solve N-Queens problem.
    """
    n = check_args()
    board = [-1] * n
    solve_nqueens(board, 0)


if __name__ == "__main__":
    main()
