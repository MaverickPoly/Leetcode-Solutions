#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        perfect = list(range(0, len(nums) + 1))

        for num in perfect:
            if num not in nums: return num
        
# @lc code=end

