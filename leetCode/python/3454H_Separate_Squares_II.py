"""
Problem: 3454. Separate Squares II (LeetCode, Hard)

You are given axis-aligned squares, squares[i] = [xi, yi, li] (bottom-left + side length).
Find the minimum y of a horizontal line such that the UNION area of squares above the line
equals the UNION area below the line. Overlaps are counted only once.

Key idea (Line Sweep on Y + Segment Tree on X):
- Turn each square into two events along y:
    at y = yi     : add interval [xi, xi+li)
    at y = yi+li  : remove interval [xi, xi+li)
- Sort events by y. Maintain active x-interval union length (coveredWidth) via a segment tree.
- Between prevY and current y, coveredWidth is constant, so area gained is:
    areaGain = coveredWidth * (y - prevY)
- First compute total union area with a sweep.
- Then sweep again accumulating area until reaching halfArea.
  If halfArea is reached within a slab where coveredWidth > 0, solve:
    prevY + (halfArea - accumulatedArea) / coveredWidth
  This gives the minimal y that splits the union area in half.

Complexity:
- Events: 2n (n <= 5e4). Coordinate compression over x endpoints.
- Time:  O(n log n)
- Space: O(n)
"""

from typing import List, Tuple

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # BLOQUE 1: Construcción de eventos en Y y compresión de X
        # Cada cuadrado [x, y, l] genera:
        # - Un evento de ENTRADA en y
        # - Un evento de SALIDA en y + l
        # Cada evento activa o desactiva un intervalo en X: [x, x+l)

        events: List[Tuple[int, int, int, int]] = []  # (y, delta, xl, xr)
        xs = set()  # Endpoints X para coordinate compression

        for x, y, l in squares:
            xl, xr = x, x + l
            events.append((y, +1, xl, xr))      # el intervalo entra
            events.append((y + l, -1, xl, xr))  # el intervalo sale
            xs.add(xl)
            xs.add(xr)

        # Ordenamos eventos por coordenada Y (barrido vertical)
        events.sort()

        # Compresión de coordenadas X (los únicos puntos donde cambia la cobertura)
        xs = sorted(xs)

        # Si no hay segmentos válidos, no hay área
        if not events or len(xs) < 2:
            return 0.0

        # BLOQUE 2: Inicialización del Segment Tree
        # El segment tree trabaja sobre los segmentos:
        # [xs[0], xs[1]), [xs[1], xs[2]), ...
        #
        # count[node]: cuántos intervalos cubren completamente este nodo
        # length[node]: longitud total cubierta en este nodo
        nseg = len(xs) - 1
        count = [0] * (4 * nseg)
        length = [0] * (4 * nseg)

        # BLOQUE 3: Funciones internas del Segment Tree
        def pull(node: int, lo: int, hi: int) -> None:
            """
            Recalcula la longitud cubierta del nodo actual.
            """
            if count[node] > 0:
                # Si al menos un intervalo cubre todo este rango,
                # entonces todo el segmento está cubierto
                length[node] = xs[hi + 1] - xs[lo]
            elif lo == hi:
                # Nodo hoja sin cobertura
                length[node] = 0
            else:
                # Combinar cobertura de hijos
                length[node] = length[node * 2] + length[node * 2 + 1]

        def add(node: int, lo: int, hi: int, L: int, R: int, delta: int) -> None:
            """
            Agrega o quita cobertura en el intervalo X [L, R)
            delta = +1 → agregar
            delta = -1 → quitar
            """
            # Caso sin intersección
            if R <= xs[lo] or xs[hi + 1] <= L:
                return

            # Caso cubierto completamente
            if L <= xs[lo] and xs[hi + 1] <= R:
                count[node] += delta
                pull(node, lo, hi)
                return

            # Caso parcial: propagar a hijos
            mid = (lo + hi) // 2
            add(node * 2, lo, mid, L, R, delta)
            add(node * 2 + 1, mid + 1, hi, L, R, delta)
            pull(node, lo, hi)

        def covered_width() -> int:
            """
            Devuelve el ancho total cubierto en X actualmente.
            """
            return length[1]

        # BLOQUE 4: Primer sweep — calcular el área total unida
        total_area = 0
        prev_y = events[0][0]

        for y, delta, xl, xr in events:
            # Área aportada por la franja anterior
            total_area += covered_width() * (y - prev_y)

            # Actualizamos cobertura en X
            add(1, 0, nseg - 1, xl, xr, delta)

            prev_y = y

        # Queremos dividir el área total en dos partes iguales
        half_area = total_area / 2.0

        # BLOQUE 5: Segundo sweep — encontrar el Y mínimo
        # Reiniciamos el segment tree
        count[:] = [0] * (4 * nseg)
        length[:] = [0] * (4 * nseg)

        accumulated = 0.0
        prev_y = events[0][0]

        for y, delta, xl, xr in events:
            width = covered_width()
            dy = y - prev_y

            if dy > 0 and width > 0:
                area_gain = width * dy

                # Si en esta franja cruzamos la mitad del área total,
                # calculamos el Y exacto dentro de la franja
                if accumulated + area_gain >= half_area:
                    return prev_y + (half_area - accumulated) / width

                accumulated += area_gain

            # Aplicamos eventos en Y
            add(1, 0, nseg - 1, xl, xr, delta)
            prev_y = y

        # Caso de seguridad (no debería ocurrir)
        return float(prev_y)


if __name__ == "__main__":
    s = Solution()
    assert abs(s.separateSquares([[0, 0, 1], [2, 2, 1]]) - 1.0) < 1e-5
    assert abs(s.separateSquares([[0, 0, 2], [1, 1, 1]]) - 1.0) < 1e-5
    print("Pasa")
