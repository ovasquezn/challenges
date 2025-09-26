"""
Problem: 611. Valid Triangle Number (LeetCode, Medium)

Given an integer array nums, return the number of index triplets (i < j < k)
such that nums[i], nums[j], nums[k] can be side lengths of a triangle.

Triangle condition:
For positive sides a <= b <= c, a + b > c must hold.
(If any side is 0, the triplet is invalid.)

Examples:
Input: nums = [2,2,3,4]
Output: 3
Explanation: Valid triplets by indices:
- (0,2,3): 2,3,4
- (1,2,3): 2,3,4
- (0,1,2): 2,2,3

Input: nums = [4,2,3,4]
Output: 4

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] <= 1000

-----------------------------------------------------
Approach (Sort + Two Pointers, O(n^2)):

1) Sort nums in non-decreasing order.
2) Fix the largest side c at position k (iterate k from n-1 down to 2).
3) Use two pointers on the prefix [0 .. k-1]:
   - i = 0 (smallest), j = k-1 (largest of the prefix)
   - If nums[i] + nums[j] > nums[k], then ANY index t in [i .. j-1]
     paired with j and k forms a valid triangle (because nums[t] >= nums[i]).
     So add (j - i) to the answer, and decrement j.
   - Else, increment i (to increase the sum).
4) Continue until i >= j. Sum over all k.

Why it works:
- Sorting guarantees nums[i] <= nums[j] <= nums[k].
- When nums[i] + nums[j] > nums[k], moving i right only increases the sum,
  so all pairs (i..j-1) with j are valid at once.

Time Complexity: O(n^2)
Space Complexity: O(1) extra (apart from sorting in-place)
"""

from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        count = 0

        for k in range(n - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
        return count


if __name__ == "__main__":
    s = Solution()
    assert s.triangleNumber([2,2,3,4]) == 3
    assert s.triangleNumber([4,2,3,4]) == 4
    assert s.triangleNumber([0,1,1,1]) == 1
    assert s.triangleNumber([0,0,0]) == 0 
    assert s.triangleNumber([1,1,2,3,5,8]) == 0
    print("OK")
