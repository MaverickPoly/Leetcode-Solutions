#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        uniques = list(set(nums))
        if len(uniques) >= 3: return sorted(uniques, reverse=True)[2]
        return max(nums)
        
# @lc code=end

