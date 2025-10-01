#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#

# @lc code=start
from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1

            while j >= 0 and key < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key
# @lc code=end
