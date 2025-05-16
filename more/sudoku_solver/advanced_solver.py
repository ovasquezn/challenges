# advanced_solver.py
import os
import time
from utils import print_board

iteration_count = 0  # Contador de iteraciones para el solver avanzado

def get_valid_numbers(board, row, col):
    """Devuelve una lista de números válidos para la casilla (row, col)."""
    if board[row][col] != 0:
        return []

    numbers = set(range(1, 10))

    # Eliminar números ya en la fila
    for j in range(9):
        if board[row][j] in numbers:
            numbers.discard(board[row][j])

    # Eliminar números ya en la columna
    for i in range(9):
        if board[i][col] in numbers:
            numbers.discard(board[i][col])

    # Eliminar números ya en el cuadrante 3x3
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] in numbers:
                numbers.discard(board[start_row + i][start_col + j])

    return list(numbers)

def find_best_cell(board):
    """Encuentra la casilla vacía con el menor número de opciones posibles."""
    min_options = 10
    best_cell = None

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                options = get_valid_numbers(board, row, col)
                if len(options) < min_options:
                    min_options = len(options)
                    best_cell = (row, col)
                    if min_options == 1:
                        return best_cell  # No hay mejor opción
    return best_cell

def solve_advanced(board):
    """Resuelve el Sudoku usando MRV y Forward Checking."""
    global iteration_count

    best_cell = find_best_cell(board)
    if not best_cell:
        return True  # Sudoku resuelto

    row, col = best_cell
    options = get_valid_numbers(board, row, col)

    for num in options:
        iteration_count += 1
        board[row][col] = num

        if solve_advanced(board):
            return True

        board[row][col] = 0  # Retroceder (backtrack)

    return False


# advanced_solver.py

def solve_advanced_visual(board):
    """Versión visual mejorada de solve_advanced con colores y contador."""
    global iteration_count

    best_cell = find_best_cell(board)
    if not best_cell:
        return True  # Sudoku resuelto

    row, col = best_cell
    options = get_valid_numbers(board, row, col)

    for num in options:
        iteration_count += 1
        board[row][col] = num

        # 👇 Mostrar avance (verde)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board, highlight=(row, col), action="place", iteration_count=iteration_count)
        time.sleep(0.05)

        if solve_advanced_visual(board):
            return True

        # 👇 Antes de borrar, guardar el número temporalmente
        temp = board[row][col]

        # Mostrar retroceso (rojo) mostrando el número antes de borrarlo
        os.system('cls' if os.name == 'nt' else 'clear')
        print_board(board, highlight=(row, col), action="remove", iteration_count=iteration_count, temp_value=temp)
        time.sleep(0.05)

        board[row][col] = 0  # Ahora sí, borrar realmente

    return False
