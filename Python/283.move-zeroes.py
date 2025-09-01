#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert = 0

        for num in nums:
            if num != 0:
                nums[insert] = num
                insert += 1
        
        while insert < len(nums):
            nums[insert] = 0
            insert += 1
        
# @lc code=end

