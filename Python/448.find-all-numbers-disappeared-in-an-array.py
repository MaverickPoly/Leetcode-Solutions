#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in num_set:
                res.append(i)
        return res
        
# @lc code=end

