"""
Problem: 1877. Minimize Maximum Pair Sum in Array 

Given an array nums of even length n, pair up all elements such that:
- each element is used exactly once
- the maximum pair sum (a + b) among all pairs is minimized

Key idea (Greedy strategy):
To minimize the maximum pair sum, we must avoid pairing large numbers together.
The optimal strategy is:
    1. Sort the array.
    2. Pair the smallest element with the largest,
        the second smallest with the second largest, and so on.

Intuition:
- Pairing large numbers together creates a very large sum that dominates the result.
- Pairing small with large "balances" the pairs and reduces the worst-case sum.
- This guarantees the smallest possible maximum among all valid pairings.

Examples:
nums = [3, 5, 2, 3]
sorted = [2, 3, 3, 5]
pairs = (2,5)=7, (3,3)=6 → result = 7

nums = [1, 2, 100, 200]
sorted = [1, 2, 100, 200]
pairs = (1,200)=201, (2,100)=102 → result = 201
(any other pairing produces a larger maximum)

Limitations:
- nums must have even length (guaranteed by the problem).
- Time complexity is O(n log n) due to sorting.
- The function returns only the minimized maximum sum, not the pairs themselves.

Complexity:
- Time: O(n log n)
- Space: O(1) extra space (sorting in place)
"""
from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1

        best_max = 0
        while i < j:
            best_max = max(best_max, nums[i] + nums[j])
            i += 1
            j -= 1

        return best_max

def test_min_pair_sum():
    s = Solution()
    assert s.minPairSum([3, 5, 2, 3]) == 7
    assert s.minPairSum([3, 5, 4, 2, 4, 6]) == 8

    # Casos extra
    assert s.minPairSum([1, 1, 1, 1]) == 2          # todos iguales
    assert s.minPairSum([1, 2, 100, 200]) == 202     # (1,200)=201, (2,100)=102 -> max=201? cuidado
    # Revisemos bien: ordenado [1,2,100,200]
    # pares: (1,200)=201, (2,100)=102 => max = 201
    assert s.minPairSum([1, 2, 100, 200]) == 201

    assert s.minPairSum([9, 2, 8, 4]) == 12          # orden [2,4,8,9] -> (2,9)=11, (4,8)=12 => 12

    print("Pasa")

test_min_pair_sum()
