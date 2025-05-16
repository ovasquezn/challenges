# utils.py

from colorama import init, Fore, Style

init(autoreset=True)

def print_board(board, highlight=None, action="place", iteration_count=None, temp_value=None):
    """Print the Sudoku board with optional highlighting and iteration counter."""
    if iteration_count is not None:
        print(f"Iteraciones: {iteration_count}\n")  # Mostrar iteraciones en vivo

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            num = board[i][j]

            if highlight and (i, j) == highlight:
                if action == "place" and num != 0:
                    print(Fore.GREEN + f"{num}", end=" ")
                elif action == "remove":
                    # 👇 Mostrar el número temporal si existe
                    if temp_value is not None:
                        print(Fore.RED + f"{temp_value}", end=" ")
                    else:
                        print(".", end=" ")
                else:
                    print(num if num != 0 else ".", end=" ")
            else:
                print(num if num != 0 else ".", end=" ")
        print()
