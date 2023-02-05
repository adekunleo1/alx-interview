#!/usr/bin/python3

import sys


def getinput():
"""Returns the size of of the dashboard"""
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n

def solve_n_queens(n):
    def can_place(row, col):
        # check if there's a queen in the same column
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(row = 0, count = 0):
        if row == n:
            result.append(board[:])
            return

        for col in range(n):
            if can_place(row, col):
                board[row] = col
                backtrack(row + 1, count + 1)

    result = []
    board = [-1 for i in range(n)]
    backtrack()
    return result

def print_result(result, n):
    for solution in result:
        for i in solution:
            print("".join("Q" + "." * (i) + "Q" + "." * (n - i - 1)))
        print("")

    result = solve_n_queens(n)
    print_result(result, n)
