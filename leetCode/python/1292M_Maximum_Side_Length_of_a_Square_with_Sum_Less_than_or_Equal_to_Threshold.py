"""
1292. Maximum Side Length of a Square with Sum <= Threshold

Goal:
Find the maximum side length k of an axis-aligned k x k square submatrix
whose sum is <= threshold. Return 0 if none exists.

Key technique: 2D Prefix Sum (summed-area table)
- Build prefix sums so any sub-rectangle sum can be queried in O(1).
- Because all values are non-negative, feasibility is monotonic:
    if a k x k square can fit under threshold, any smaller square can too.
    This allows binary search on k.

Steps:
1) Build prefix matrix ps of size (m+1) x (n+1):
    ps[r+1][c+1] stores sum of mat[0..r][0..c]
2) Function can(k):
    checks all k x k squares and returns True if any has sum <= threshold
3) Binary search k in [0, min(m,n)]

Time:
- Build prefix: O(m*n)
- Each can(k): O(m*n) (scan all top-left positions)
- Binary search adds log(min(m,n)) factor
Total: O(m*n*log(min(m,n)))  <= 300*300*~9 OK.

Space: O(m*n) for prefix sums.
"""

from typing import List

class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m):
            row_acc = 0
            for c in range(n):
                row_acc += mat[r][c]
                ps[r + 1][c + 1] = ps[r][c + 1] + row_acc

        def rect_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            return ps[r2][c2] - ps[r1][c2] - ps[r2][c1] + ps[r1][c1]

        def can(k: int) -> bool:
            if k == 0:
                return True
            for r in range(0, m - k + 1):
                r2 = r + k
                for c in range(0, n - k + 1):
                    c2 = c + k
                    if rect_sum(r, c, r2, c2) <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

if __name__ == "__main__":
    s = Solution()
    mat1 = [
        [1,1,3,2,4,3,2],
        [1,1,3,2,4,3,2],
        [1,1,3,2,4,3,2],
    ]
    assert s.maxSideLength(mat1, 4) == 2
    mat2 = [[2]*5 for _ in range(5)]
    assert s.maxSideLength(mat2, 1) == 0
    assert s.maxSideLength([[0,0],[0,0]], 0) == 2
    print("Pasa")
