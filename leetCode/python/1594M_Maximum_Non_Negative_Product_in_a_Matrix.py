"""
LeetCode 1594. Maximum Non Negative Product in a Matrix (Medium)

You are given a m x n matrix grid. Initially, you are located at the top-left 
corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in 
the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative 
product. The product of a path is the product of all integers in the grid cells 
visited along the path.

Return the maximum non-negative product modulo 10^9 + 7. If the maximum product 
is negative, return -1.

IMPORTANT:
- The modulo is applied AFTER computing the maximum product.
- Grid values can be negative, zero, or positive.

------------------------------------------------------------

APPROACH: Dynamic Programming (Max + Min Tracking)

Key Insight:
Because the grid contains negative numbers, we must track BOTH:
- The maximum product up to each cell
- The minimum product up to each cell

Why?
A negative * negative = positive → a minimum value can become the maximum later.

State Definition:
- max_dp[i][j]: maximum product to reach cell (i, j)
- min_dp[i][j]: minimum product to reach cell (i, j)

Transition:
From each cell, we can come from:
- top (i-1, j)
- left (i, j-1)

We compute:
candidates = [
    max_dp[i-1][j] * value,
    min_dp[i-1][j] * value,
    max_dp[i][j-1] * value,
    min_dp[i][j-1] * value
]

Then:
- max_dp[i][j] = max(candidates)
- min_dp[i][j] = min(candidates)

Base Case:
max_dp[0][0] = grid[0][0]
min_dp[0][0] = grid[0][0]

Time Complexity: O(m * n)
Space Complexity: O(m * n)

------------------------------------------------------------

EDGE CASES:
- If final result is negative → return -1
- If result is zero → valid (return 0)
- Do NOT apply modulo during DP (breaks sign logic)

------------------------------------------------------------
"""

from typing import List
import pytest

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows = len(grid)
        cols = len(grid[0])

        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]

        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        for i in range(1, rows):
            value = grid[i][0]
            max_dp[i][0] = max_dp[i - 1][0] * value
            min_dp[i][0] = min_dp[i - 1][0] * value

        for j in range(1, cols):
            value = grid[0][j]
            max_dp[0][j] = max_dp[0][j - 1] * value
            min_dp[0][j] = min_dp[0][j - 1] * value

        for i in range(1, rows):
            for j in range(1, cols):
                value = grid[i][j]

                candidates = [
                    max_dp[i - 1][j] * value,
                    min_dp[i - 1][j] * value,
                    max_dp[i][j - 1] * value,
                    min_dp[i][j - 1] * value,
                ]

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        result = max_dp[rows - 1][cols - 1]

        if result < 0:
            return -1

        return result % MOD

def run_tests():
    solution = Solution()

    test_cases = [
        ("all_negative", [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]], -1),
        ("positive_case", [[1, -2, 1], [1, -2, 1], [3, -4, 1]], 8),
        ("zero_case", [[1, 3], [0, -4]], 0),
        ("single_positive", [[5]], 5),
        ("single_negative", [[-5]], -1),
    ]

    for name, grid, expected in test_cases:
        result = solution.maxProductPath(grid)

        assert result == expected, (
            f"\nTest failed: {name}\n"
            f"Input: {grid}\n"
            f"Expected: {expected}\n"
            f"Got: {result}"
        )

        print(f"Passed: {name}")

    print("\nAll tests passed.")

@pytest.mark.parametrize(
    "grid, expected",
    [
        (
            [[-1, -2, -3], [-2, -3, -3], [-3, -3, -2]],
            -1,
        ),
        (
            [[1, -2, 1], [1, -2, 1], [3, -4, 1]],
            8,
        ),
        (
            [[1, 3], [0, -4]],
            0,
        ),
        (
            [[5]],
            5,
        ),
        (
            [[-5]],
            -1,
        ),
    ],
)
def test_max_product_path(grid, expected):
    assert Solution().maxProductPath(grid) == expected

if __name__ == "__main__":
    run_tests()

