import time
import os
from utils import print_board
iteration_count = 0  # Contador global de intentos

def is_valid(board, row, col, num):
    """Check if placing num at (row, col) is valid."""
    # Verificar fila
    for i in range(9):
        if board[row][i] == num:
            return False

    # Verificar columna
    for i in range(9):
        if board[i][col] == num:
            return False

    # Verificar cuadrante 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve(board):
    global iteration_count
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    iteration_count += 1  # 👈 Aumentamos cada intento
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# solver.py

import time
import os
from utils import print_board

def solve_visual(board):
    global iteration_count
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    iteration_count += 1  # 👈 También contamos en modo visual
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_board(board, highlight=(row, col))
                        time.sleep(0.05)

                        if solve_visual(board):
                            return True
                        board[row][col] = 0

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_board(board, highlight=(row, col))
                        time.sleep(0.05)
                return False
    return True