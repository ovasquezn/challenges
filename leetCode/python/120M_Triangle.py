"""
Problem: 120. Triangle (LeetCode, Medium)

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below.
More formally, if you are on index i on the current row, you may move
to either index i or index i + 1 on the next row.

-----------------------------------------------------
Examples:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation:
   2
  3 4
 6 5 7
4 1 8 3

Minimum path sum = 2 + 3 + 5 + 1 = 11

Input: triangle = [[-10]]
Output: -10

-----------------------------------------------------
Constraints:
- 1 <= triangle.length <= 200
- triangle[0].length == 1
- triangle[i].length == triangle[i-1].length + 1
- -10^4 <= triangle[i][j] <= 10^4

-----------------------------------------------------
Approach:
We use Dynamic Programming (bottom-up).
Start from the last row and move upwards:
    dp[j] = triangle[i][j] + min(dp[j], dp[j+1])

The final answer will be in dp[0].

Time Complexity: O(n^2)
Space Complexity: O(n), where n is the number of rows.
"""

from typing import List

def minimumTotal(triangle: List[List[int]]) -> int:
    # Copia de la última fila como DP
    dp = triangle[-1][:]

    # Recorre desde la fila n-2 hasta la 0
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

    return dp[0]

print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))  # 11
print(minimumTotal([[-10]]))                        # -10
