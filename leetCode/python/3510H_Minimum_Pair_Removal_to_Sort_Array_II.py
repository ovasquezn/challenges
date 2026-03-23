"""
3510. Minimum Pair Removal to Sort Array II

We are given an array nums (n up to 1e5). We can repeat this deterministic operation:
- Select the adjacent pair with the minimum sum in the current array.
- If multiple pairs tie, pick the leftmost such pair.
- Replace the pair by their sum (array length decreases by 1).

Return the number of operations needed until the array becomes non-decreasing.

Key observations:
- The rule is deterministic, so the number of operations is exactly the number of merges
  until the array first becomes non-decreasing.
- A direct simulation must be efficient:
  * We need to repeatedly extract the minimum-sum adjacent pair with leftmost tie-break.
  * We need to know when the array is non-decreasing without rescanning O(n) each time.

Approach (O(n log n)):
1) Represent the array as a doubly-linked list over the original indices.
   Merging two adjacent nodes keeps the left node's index as the "position", and removes the right.
   => The order of nodes is always the original index order, so "leftmost" tie-break is simply
      the smallest left index among tied pairs.
2) Maintain a min-heap of current adjacent pairs keyed by:
      (sum = val[i] + val[next[i]], left_index = i)
   Use lazy deletion with a "stamp" per left node to invalidate outdated heap entries.
3) Maintain bad_count = number of "descending edges" (val[i] > val[next[i]]) in the current list.
   The array is non-decreasing iff bad_count == 0.
   Each merge only affects O(1) local edges, so we update bad_count in O(1).

Time:  O((n + merges) log n) <= O(n log n)
Space: O(n)
"""

from typing import List
import heapq

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        prev = [-1] * n
        nxt = [-1] * n
        alive = [True] * n
        val = nums[:]

        for i in range(n):
            if i > 0:
                prev[i] = i - 1
            if i < n - 1:
                nxt[i] = i + 1

        def bad_edge(i: int, j: int) -> int:
            return 1 if val[i] > val[j] else 0

        bad_count = 0
        for i in range(n - 1):
            bad_count += bad_edge(i, i + 1)

        if bad_count == 0:
            return 0

        stamp = [0] * n

        heap = []
        for i in range(n - 1):
            s = val[i] + val[i + 1]
            heapq.heappush(heap, (s, i, stamp[i]))

        ops = 0

        while bad_count > 0:
            while True:
                pair_sum, i, st = heapq.heappop(heap)
                if not alive[i]:
                    continue
                if stamp[i] != st:
                    continue
                j = nxt[i]
                if j == -1 or not alive[j]:
                    continue
                break

            p = prev[i]
            r = nxt[j] 

            if p != -1:
                bad_count -= bad_edge(p, i)
            bad_count -= bad_edge(i, j)
            if r != -1:
                bad_count -= bad_edge(j, r)

            val[i] = val[i] + val[j]
            alive[j] = False

            nxt[i] = r
            if r != -1:
                prev[r] = i

            if p != -1:
                bad_count += bad_edge(p, i)
            if r != -1:
                bad_count += bad_edge(i, r)

            if p != -1:
                stamp[p] += 1
                heapq.heappush(heap, (val[p] + val[i], p, stamp[p]))

            stamp[i] += 1
            if r != -1:
                heapq.heappush(heap, (val[i] + val[r], i, stamp[i]))
            ops += 1
        return ops

def run_tests():
    sol = Solution()

    assert sol.minimumPairRemoval([5, 2, 3, 1]) == 2
    assert sol.minimumPairRemoval([1, 2, 2]) == 0

    assert sol.minimumPairRemoval([-5, -5, 0, 0, 10]) == 0

    assert sol.minimumPairRemoval([1, 2, 1, 2]) == 2

    assert sol.minimumPairRemoval([4, 3, 2, 1]) == 2

    assert sol.minimumPairRemoval([42]) == 0

    print("Pasa")
run_tests()
