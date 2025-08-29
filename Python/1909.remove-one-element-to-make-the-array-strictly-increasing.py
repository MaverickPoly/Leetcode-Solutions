#
# @lc app=leetcode id=1909 lang=python3
#
# [1909] Remove One Element to Make the Array Strictly Increasing
#

# @lc code=start
from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        removed = False
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                if removed:
                    return False

                removed = True

                if i == 0 or nums[i - 1] < nums[i + 1]:
                    continue
                elif i + 2 >= len(nums) or nums[i] < nums[i + 2]:
                    continue
                else:
                    return False
        
        return True
        
# @lc code=end

