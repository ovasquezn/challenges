# class Solution:
#     def countGoodArrays(self, n: int, m: int, k: int) -> int:
#         MOD = 10**9 + 7
#         dp_anterior = [0] * (k + 2)
#         dp_actual = [0] * (k + 2)
#         dp_anterior[0] = m

#         for longitud in range(2, n + 1):
#             for iguales in range(0, min(longitud, k + 1)):
#                 mismo = dp_anterior[iguales - 1] if iguales > 0 else 0
#                 distinto = dp_anterior[iguales] * (m - 1)
#                 dp_actual[iguales] = (mismo + distinto) % MOD
#             dp_anterior, dp_actual = dp_actual, [0] * (k + 2)
#         return dp_anterior[k] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7

        # Precálculo de factoriales y factoriales inversos
        factorial = [1] * (n)
        inv_factorial = [1] * (n)

        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i % MOD

        inv_factorial[n - 1] = pow(factorial[n - 1], MOD - 2, MOD)
        for i in range(n - 2, -1, -1):
            inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return factorial[a] * inv_factorial[b] % MOD * inv_factorial[a - b] % MOD

        combinatoria = comb(n - 1, k)
        potencias = pow(m - 1, n - 1 - k, MOD)

        return m * combinatoria % MOD * potencias % MOD