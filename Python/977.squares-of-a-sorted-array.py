#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#

# @lc code=start
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(list(map(lambda x: pow(x, 2), nums)))
        
# @lc code=end

