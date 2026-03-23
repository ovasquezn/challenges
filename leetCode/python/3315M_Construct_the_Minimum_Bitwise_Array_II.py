"""
Problem: 3315. Construct the Minimum Bitwise Array II (LeetCode – Daily Question)

Input:
Array nums of length n, where:
- nums[i] is a prime number
- 2 ≤ nums[i] ≤ 1e9

Task:
Construct an array ans of length n such that, for each index i:

    ans[i] OR (ans[i] + 1) == nums[i]

Additionally:
- ans[i] must be the minimum possible value
- If no such value exists, set ans[i] = -1

Key Observations:

1) Bitwise property:
For any integer x:
    x OR (x + 1) is always an ODD number

Reason:
- x and x + 1 differ in the least significant bit
- At least one of them has LSB = 1

Impossible Case:

If nums[i] is EVEN:
- nums[i] cannot be written as x OR (x + 1)
- Therefore, ans[i] = -1

------------------------------------------------------------

Valid Case (nums[i] is ODD):

Since nums[i] is:
- prime
- odd

We analyze its binary representation.

Key insight:
To minimize ans[i], we must remove exactly ONE set bit (1) from nums[i].

The optimal choice:
- Remove the LEAST significant set bit

Bit Manipulation Trick:

Removing the lowest set bit of a number x:

    x & (x - 1)

Final Construction Rule:

For each nums[i]:
- If nums[i] is even → ans[i] = -1
- Else → ans[i] = nums[i] & (nums[i] - 1)

Examples:

Input:
nums = [2, 3, 5, 7]

Output:
ans = [-1, 1, 4, 3]

Explanation:
1 OR 2 = 3
4 OR 5 = 5
3 OR 4 = 7

Input:
nums = [11, 13, 31]

Output:
ans = [9, 12, 15]

Time Complexity:
- O(n), single pass through the array

Space Complexity:
- O(1) extra space (excluding output)
"""

from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for p in nums:
            if (p & 1) == 0:
                ans.append(-1)
                continue
            t = 0
            x = p
            while x & 1:
                t += 1
                x >>= 1
            ans.append(p - (1 << (t - 1)))
        return ans

test1 = Solution()
print(test1.minBitwiseArray([2,3,5,7]))