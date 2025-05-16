# Sudoku Solver (Python)

Un pequeño proyecto para resolver tableros de Sudoku utilizando la técnica de Backtracking.

## Cómo ejecutar

1. Asegúrate de tener Python 3 instalado.
2. Clona o descarga este repositorio.
3. Corre el programa:

```bash
python main.py
```

## ¿Cómo se aplica backtracking al Sudoku?

Para resolver un Sudoku utilizando backtracking, seguimos este enfoque:

* Buscar una casilla vacía:
    *  Recorremos el tablero fila por fila, columna por columna, hasta encontrar un lugar con valor 0 (o vacío).
* Intentar colocar un número:
    * Probamos colocar números del 1 al 9 en esa casilla vacía.

* Validar la colocación:
    * Verificamos si el número colocado:
    * No se repite en la misma fila,
    * No se repite en la misma columna,
    * No se repite en el mismo cuadro 3x3.

* Avanzar o retroceder:
    * Si el número cumple con todas las condiciones, colocamos el número y continuamos buscando la siguiente casilla vacía (avance).
    * Si en algún punto no podemos colocar ningún número válido, retrocedemos (backtrack), deshaciendo la última colocación y probando el siguiente número disponible.
* Finalizar:
    * El algoritmo termina cuando:
        * Todas las casillas están llenas y el Sudoku es válido (solución encontrada).
        * Se han probado todas las combinaciones posibles y no existe solución (sin solución).
  
## Sudoku Solver Avanzado (MRV + Forward Checking)

¿Qué problema mejora respecto al solver básico?

El solver básico recorre el tablero de izquierda a derecha y de arriba a abajo, intentando todos los números posibles para cada celda vacía.
Este enfoque puede generar muchos caminos erróneos, llevando a un número elevado de iteraciones y retrocesos (backtracking).

El solver avanzado introduce estrategias para reducir dramáticamente el espacio de búsqueda y hacer más inteligente el proceso de decisión.

### Minimum Remaining Values (MRV)

MRV es una heurística de selección de variables.

Consiste en elegir primero la casilla vacía que tiene menos opciones válidas para llenarse.

Cuanto menos opciones tiene una casilla, más urgente es decidir su valor correctamente, porque puede bloquear el Sudoku si no se llena bien.

Beneficio: Reduce rápidamente las ramificaciones erróneas al atacar primero las áreas más críticas.

## Forward Checking (simple)

Después de colocar un número en una celda, verificamos de inmediato que las demás casillas aún tengan posibles opciones válidas.

Si colocar un número deja a otra celda sin opciones, retrocedemos inmediatamente sin profundizar más en un camino imposible.
Beneficio:

Evita avanzar en caminos muertos, reduciendo retrocesos profundos.

## Comparativa de Rendimiento

### Metodología de Prueba
Se resolvieron Sudokus usando el solver básico (backtracking puro) y el solver avanzado (MRV + Forward Checking). Se midieron tiempo de ejecución e iteraciones.

### Resultados

| Tablero | Método | Tiempo (s) | Iteraciones |
|:---|:---|:---|:---|
| Fácil | Básico | XX | XX |
| Fácil | Avanzado | XX | XX |

### Análisis
- El solver avanzado reduce hasta un XX% las iteraciones.
- El tiempo de resolución mejora entre X y X.
- En dificultades altas, el solver avanzado mantiene tiempos manejables, mientras que el básico se vuelve ineficiente.

### Conclusiones
- MRV y Forward Checking son esenciales para resolver Sudokus difíciles de forma eficiente.
- El solver avanzado es mucho más efectivo y escalable que el método clásico de backtracking puro.
