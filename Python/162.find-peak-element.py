#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        for i in range(len(nums)):
            if i == 0 and nums[i] > nums[i + 1]:
                return 0
            elif i == len(nums) - 1 and nums[i] > nums[i - 1]:
                return len(nums) - 1
            else:
                if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                    return i
        return 0
# @lc code=end

