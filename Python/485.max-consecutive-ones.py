#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        return len(max("".join(list(map(str, nums))).split("0")))
        
# @lc code=end

