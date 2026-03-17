#!/usr/bin/env python3
"""
N-Queens Problem Solver using Backtracking with Step-by-Step CLI Visualization.

This script solves the N-Queens problem for a given board size N using backtracking.
It prints the board state at each major step, including placements, conflicts, and backtracks.
Visualizes the chessboard with 'Q' for queens, '.' for empty, and row/col numbers.
"""

def print_board(board, n, step_msg="Current board state"):
    """
    Print the chessboard in a simple CLI format with step message.
    """
    print("\n" + "="*50)
    print(f"{step_msg}")
    print("="*50)
    header = "   " + " ".join([str(i).rjust(2) for i in range(n)])
    print(header)
    for i in range(n):
        row_str = f"{i}: " + "".join(["Q " if board[i] == j else ". " for j in range(n)])
        print(row_str.rstrip())
    print("="*50 + "\n")

def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col].
    """
    # Check upper left diagonal
    for i, j in enumerate(board[:row]):
        if j == col or (row - i) == (col - j):
            return False
    # Check upper right diagonal
    for i, j in enumerate(board[:row]):
        if j == col or (row - i) == (j - col):
            return False
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    return True

def solve_n_queens_util(board, row, n, steps):
    """
    Recursive backtracking utility.
    steps: list to track and print solving steps.
    """
    if row == n:
        steps.append(("SOLVED", board[:]))
        return True
    
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            step_msg = f"Step {len(steps)+1}: Placed queen at row {row}, col {col}"
            steps.append((step_msg, board[:]))
            print_board(board, n, step_msg)
            
            if solve_n_queens_util(board, row + 1, n, steps):
                return True
            
            # Backtrack
            board[row] = -1
            step_msg = f"Backtracking from row {row}, col {col} (conflict found deeper)"
            steps.append((step_msg, board[:]))
            print_board(board, n, step_msg)
    
    return False

def solve_n_queens(n):
    """
    Main solver function.
    """
    board = [-1] * n
    steps = []
    
    print(f"Solving {n}-Queens problem using Backtracking...")
    print_board(board, n, "Initial empty board")
    
    if solve_n_queens_util(board, 0, n, steps):
        print_board(board, n, "Solution found!")
        print("Queens positions (row -> col):", board)
        return True
    else:
        print("No solution exists.")
        return False

if __name__ == "__main__":
    # Solve for N=4 (classic example with visualization)
    solve_n_queens(4)
    
    # Uncomment to try larger N (less verbose output for bigger boards)
    # solve_n_queens(8)

