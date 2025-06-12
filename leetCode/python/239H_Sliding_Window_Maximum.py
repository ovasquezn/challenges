# You are given an array of integers nums, there is a sliding window of size k which is moving from 
# the very left of the array to the very right. You can only see the k numbers in the window. 
# Each time the sliding window moves right by one position.

# Return the max sliding window.

# Example 1:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
 
# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# 1 <= k <= nums.length

from typing import List

# Complejidad O(n*k), solución no eficiente
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Si n = 10_000 y k = 100 serán 1_000_000 operaciones
        """
        temp = []
        # O(n) iteraciones.
        for i in range(len(nums)-k+1):
            # Encontrar el máximo en una lista de tamaño k es una operación de O(k).
            temp.append(max(nums[i:i+k]))
        return temp

# Complejidad O(n), mucho mejor
class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = []

        for i in range(len(nums)):
            # Elimina los índices que están fuera del rango de la ventana
            if window and window[0] < i - k + 1:
                window.pop(0)

            # Elimina del final los índices cuyos valores son menores al actual
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result

Test = Solution()
Test1 = Solution2()

print(Test.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Test.maxSlidingWindow([1], 1))

print(Test1.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Test1.maxSlidingWindow([1], 1))

# Test de redimiento
import time
import random

# Crear instancia
test_brute = Solution()
test_optimized = Solution2()

nums = [random.randint(-1000, 1000) for _ in range(10000)]
k = 100

# O(n * k)
start = time.time()
res_brute = test_brute.maxSlidingWindow(nums, k)
end = time.time()
print(f"O(n*k): {end - start:.4f} segundos")

# O(n)
start = time.time()
res_optimized = test_optimized.maxSlidingWindow(nums, k)
end = time.time()
print(f"O(n):    {end - start:.4f} segundos")

print("Resultados iguales:", res_brute == res_optimized)

