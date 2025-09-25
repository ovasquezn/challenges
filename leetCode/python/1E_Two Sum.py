"""
Problem: 1. Two Sum (LeetCode, Easy)

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

-----------------------------------------------------
Examples:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] = 9

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]

-----------------------------------------------------
Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Exactly one valid answer exists.

-----------------------------------------------------
Approach:
We use a hash map (dictionary) to store previously seen numbers and their indices.
For each element 'num', we check if (target - num) already exists in the map.
If yes, we found the solution. Otherwise, we store num in the map.

Time Complexity: O(n)
Space Complexity: O(n)
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in values:
                return [values[complement], i]
            values[num] = i