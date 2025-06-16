# Connet Four
# Explicación:
# El juego de Conecta Cuatro se juega en un tablero de 6 filas por 7 columnas.
# El objetivo es alinear cuatro fichas del mismo color en línea recta, ya sea horizontal, vertical o diagonalmente.

def who_is_winner(pieces_position_list):
    # Paso 1: Crear tablero vacío (6 filas, 7 columnas)
    ROWS, COLS = 6, 7
    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    
    # Mapeo de columnas: A -> 0, B -> 1, ..., G -> 6
    col_map = {chr(ord('A') + i): i for i in range(COLS)}

    # Función para insertar ficha en el tablero
    def drop_piece(column, color):
        col_index = col_map[column]
        for row in reversed(range(ROWS)):  # De abajo hacia arriba
            if board[row][col_index] == "":
                board[row][col_index] = color
                return row, col_index  # Posición donde cayó la ficha

    # Función para revisar si hay 4 en línea desde (r, c)
    def check_winner(r, c, color):
        directions = [
            (1, 0),   # vertical
            (0, 1),   # horizontal
            (1, 1),   # diagonal ↘
            (1, -1)   # diagonal ↙
        ]
        for dr, dc in directions:
            count = 1
            # Revisar en dirección positiva
            for i in range(1, 4):
                nr, nc = r + dr*i, c + dc*i
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == color:
                    count += 1
                else:
                    break
            # Revisar en dirección negativa
            for i in range(1, 4):
                nr, nc = r - dr*i, c - dc*i
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == color:
                    count += 1
                else:
                    break
            if count >= 4:
                return True
        return False

    # Simular todas las jugadas
    for move in pieces_position_list:
        col_letter, color = move.split("_")
        row, col = drop_piece(col_letter, color)
        if check_winner(row, col, color):
            return color

    return "Draw"
