"""
2975. Maximum Square Area by Removing Fences From a Field

We have a rectangle with fixed boundary fences at x=1 and x=m, y=1 and y=n.
Internal fences exist at positions in hFences (horizontal lines) and vFences (vertical lines).
By removing some internal fences, we can create a larger rectangular region whose height is the
distance between two chosen horizontal fences, and width is the distance between two chosen vertical fences.

A square is possible iff there exists a distance d that can be achieved both:
- as a difference between two horizontal fence positions
- as a difference between two vertical fence positions

Approach:
- Add boundaries (1 and m) to horizontal fences; (1 and n) to vertical fences
- Compute all pairwise distances for each list (O(k^2), k <= 602)
- Find the maximum common distance d between the two distance sets
- Answer is d^2 mod (1e9+7), or -1 if no common distance exists

Time:  O(H^2 + V^2) <= ~2 * 181k operations
Space: O(#distinct distances)
"""

from typing import List

class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        H = sorted(hFences + [1, m])
        V = sorted(vFences + [1, n])
        def all_distances(arr: List[int]) -> set:
            dists = set()
            L = len(arr)
            for i in range(L):
                ai = arr[i]
                for j in range(i + 1, L):
                    dists.add(arr[j] - ai)
            return dists
        h_dists = all_distances(H)
        v_dists = all_distances(V)
        common = h_dists & v_dists
        if not common:
            return -1
        d = max(common)
        return (d * d) % MOD

if __name__ == "__main__":
    s = Solution()
    assert s.maximizeSquareArea(4, 3, [2, 3], [2]) == 4
    assert s.maximizeSquareArea(6, 7, [2], [4]) == -1
    assert s.maximizeSquareArea(5, 5, [2, 4], [2, 4]) == 16 
    print("Pasa")
