"""
3314. Construct the Minimum Bitwise Array I (LeetCode, Easy)

Given an array nums of prime integers, construct ans where for each i:
    ans[i] OR (ans[i] + 1) == nums[i]
and ans[i] is minimized. If impossible, ans[i] = -1.

Key insight:
- Let p = nums[i].
- If p is even, it's impossible (because x OR (x+1) is always odd), so return -1.
- For odd p, count how many trailing 1 bits p has (t >= 1).
    The minimal solution is:
        ans = p - 2^(t-1)

Why:
- Choose k = t-1 (highest bit within the trailing-ones block).
- Set ans = p with bit k turned off.
- Then ans+1 turns that bit back on and clears lower bits, and OR reconstructs p.

Constraints are small, but this solution is O(1) per number.
"""


from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def trailing_ones(x: int) -> int:
            cnt = 0
            while x & 1:
                cnt += 1
                x >>= 1
            return cnt

        ans = []
        for p in nums:
            if p % 2 == 0:
                ans.append(-1)
                continue
            t = trailing_ones(p)
            ans.append(p - (1 << (t - 1)))
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.minBitwiseArray([2, 3, 5, 7]) == [-1, 1, 4, 3]
    assert s.minBitwiseArray([11, 13, 31]) == [9, 12, 15]
    print("Pasa")
