#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i + 1:])
            if left == right:
                return i

        return -1
        
        
# @lc code=end

