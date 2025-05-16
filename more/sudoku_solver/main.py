# main.py

import time
import solver
import advanced_solver
from utils import print_board
from board_examples import easy_board, medium_board, hard_board, extreme_board

def input_custom_board():
    """Permite al usuario ingresar un tablero de Sudoku."""
    print("\nIngresa tu Sudoku fila por fila.")
    print("Escribe 9 números separados por espacios.")
    print("Usa 0 para casillas vacías.")
    
    board = []
    for i in range(9):
        while True:
            try:
                row = input(f"Fila {i+1}: ").strip().split()
                if len(row) != 9:
                    raise ValueError("Debes ingresar exactamente 9 números.")
                row = [int(num) for num in row]
                if not all(0 <= num <= 9 for num in row):
                    raise ValueError("Sólo se permiten números entre 0 y 9.")
                board.append(row)
                break
            except ValueError as e:
                print(f"Error: {e}")
    return board

def main():
    print("¿Qué quieres hacer?")
    print("1. Usar un tablero de ejemplo")
    print("2. Ingresar mi propio tablero")
    
    mode = input("Ingresa 1 o 2: ")
    
    if mode == "1":
        print("\nSelecciona un Sudoku para resolver:")
        print("1. Fácil")
        print("2. Intermedio")
        print("3. Difícil")
        print("4. Extremadamente difícil")
        
        choice = input("Ingresa el número de tu elección: ")
        
        if choice == "1":
            board = easy_board
        elif choice == "2":
            board = medium_board
        elif choice == "3":
            board = hard_board
        elif choice == "4":
            board = extreme_board
        else:
            print("Elección inválida. Usando el tablero fácil por defecto.")
            board = easy_board
    elif mode == "2":
        board = input_custom_board()
    else:
        print("Elección inválida. Usando el tablero fácil por defecto.")
        board = easy_board

    print("\n¿Con qué solver quieres resolver?")
    print("1. Solver Básico (Backtracking puro)")
    print("2. Solver Avanzado (MRV + Forward Checking)")

    solver_choice = input("Ingresa 1 o 2: ")

    print("\nSudoku Original:")
    print_board(board)

    # Resetear contadores
    solver.iteration_count = 0
    advanced_solver.iteration_count = 0

    print("\n¿Quieres visualizar la resolución paso a paso? (s/n)")
    visual_mode = input().lower()

    start_time = time.time()

    if solver_choice == "1":
        if visual_mode == "s":
            success = solver.solve_visual(board)
        else:
            success = solver.solve(board)
        iteraciones = solver.iteration_count
    else:
        if visual_mode == "s":
            success = advanced_solver.solve_advanced_visual(board)
        else:
            success = advanced_solver.solve_advanced(board)
        iteraciones = advanced_solver.iteration_count

    end_time = time.time()

    if success:
        print("\nSudoku Resuelto:")
        print_board(board)
        print(f"\nTiempo de ejecución: {end_time - start_time:.6f} segundos")
        print(f"Total de iteraciones: {iteraciones}")
    else:
        print("No se encontró solución.")
        print(f"\nTiempo de ejecución: {end_time - start_time:.6f} segundos")
        print(f"Total de iteraciones: {iteraciones}")

if __name__ == "__main__":
    main()
