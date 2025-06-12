# Longest Common Subsequence

# Write a function called LCS that accepts two sequences and returns the longest subsequence common to the passed in sequences.

# Subsequence

# A subsequence is different from a substring. The terms of a subsequence need not be consecutive terms of the original sequence.

# Example subsequence

# Subsequences of "abc" = "a", "b", "c", "ab", "ac", "bc" and "abc".

# LCS examples

# lcs( "abcdef" , "abc" ) => returns "abc"
# lcs( "abcdef" , "acf" ) => returns "acf"
# lcs( "132535365" , "123456789" ) => returns "12356"

# Notes

# Both arguments will be strings
# Return value must be a string
# Return an empty string if there exists no common subsequence
# Both arguments will have one or more characters (in JavaScript)
# All tests will only have a single longest common subsequence. Don't worry about cases such as LCS( "1234", "3412" ), which would have two possible longest common subsequences: "12" and "34".

# Note that the Haskell variant will use randomized testing, but any longest common subsequence will be valid.

# Note that the OCaml variant is using generic lists instead of strings, and will also have randomized tests (any longest common subsequence will be valid).

# Solution

# Solución recursiva
# Explicación:
# La solución recursiva es simple, si los últimos caracteres de las dos cadenas son iguales, entonces el último carácter debe ser parte de la LCS. Por lo tanto, se llama a la función recursiva sin los últimos caracteres de ambas cadenas. Si los últimos caracteres no son iguales, entonces la LCS debe ser la máxima de las dos subsecuencias eliminando el último carácter de la primera cadena y la segunda cadena.

# Solución con programación dinámica
# Explicación:
# La solución con programación dinámica es simple, se crea una matriz dp de tamaño (m + 1) x (n + 1) donde m y n son las longitudes de las dos cadenas. dp[i][j] representa la longitud de la LCS de las primeras i caracteres de la primera cadena y las primeras j caracteres de la segunda cadena.

def lcs(x, y):
    if not x or not y:
        return ''
    if x[-1] == y[-1]:
        return lcs(x[:-1], y[:-1]) + x[-1]
    else:
        return max(lcs(x, y[:-1]), lcs(x[:-1], y), key=len)

def lcs_v2(s1, s2):
    m, n = len(s1), len(s2)
    
    # Crear la matriz dp con ceros:
    # Creamos una matriz dp de tamaño (m+1) x (n+1), llena de ceros.
    # dp[i][j] guardará la longitud de la LCS entre s1[:i] y s2[:j].
    # Agregamos una fila y una columna extra para manejar casos base cuando una cadena está vacía.
    
    # Ejemplo con s1 = "abc", s2 = "ac":
    #    ''  a  c
    # ''  0  0  0
    # a   0  0  0
    # b   0  0  0
    # c   0  0  0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Llenar la tabla usando programación dinámica:
    # Si los caracteres s1[i-1] y s2[j-1] son iguales, heredamos dp[i-1][j-1] y sumamos 1, porque extendemos la subsecuencia.
    # Si los caracteres son diferentes, tomamos el máximo entre:
    # dp[i-1][j] (ignoramos el carácter de s1)
    # dp[i][j-1] (ignoramos el carácter de s2)
    # Ejemplo: Para s1 = "abc", s2 = "ac", la matriz dp se llena así:
    #    ''  a  c
    # ''  0  0  0
    # a   0  1  1
    # b   0  1  1
    # c   0  1  2
    
    # a == a → dp[1][1] = dp[0][0] + 1 = 1
    # b != c → dp[2][2] = max(dp[1][2], dp[2][1]) = 1
    # c == c → dp[3][2] = dp[2][1] + 1 = 2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


    
    # Reconstrucción de la LCS desde la tabla dp:        
    # Empezamos desde dp[m][n] y seguimos las pistas para reconstruir la LCS.
    # Si s1[i-1] == s2[j-1], significa que ese carácter está en la LCS, lo agregamos y nos movemos diagonalmente (i-1, j-1).
    # Si dp[i-1][j] > dp[i][j-1], nos movemos hacia arriba (i-1).
    # Si dp[i][j-1] >= dp[i-1][j], nos movemos a la izquierda (j-1).
    # Ejemplo s1 = "abc", s2 = "ac":
    # c == c → Agregar c, mover (i=2, j=1)
    # b != a → dp[1][1] > dp[2][0], mover (i=1, j=1)
    # a == a → Agregar a, mover (i=0, j=0)
    # Lista lcs_string = ['c', 'a'], invertirla: "ac".
    lcs_string = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_string.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # Invertir la lista lcs_string y unirla en una cadena.
    return "".join(reversed(lcs_string))


from functools import lru_cache

@lru_cache(None)
def lcs_v3(x, y):
    if not x or not y:
        return ''
    if x[-1] == y[-1]:
        return lcs_v3(x[:-1], y[:-1]) + x[-1]
    return max(lcs_v3(x, y[:-1]), lcs_v3(x[:-1], y), key=len)

print(lcs("abcdef", "acf"))  # "acf"
# Test Cases
print(
    lcs("abcdef", "abc"),
    lcs("abcdef", "acf"),
    lcs("132535365", "123456789")
)

print(
    lcs_v2("abcdef", "abc"),
  #  lcs_v2("abcdef", "acf"),
  #  lcs_v2("132535365", "123456789")
)