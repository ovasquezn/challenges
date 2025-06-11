# 3151 - Special Array I
# 10/06/25

class Solution:
    def isArraySpecial(self, nums):
        for i in range(len(nums) - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
