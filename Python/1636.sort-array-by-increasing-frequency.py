#
# @lc app=leetcode id=1636 lang=python3
#
# [1636] Sort Array by Increasing Frequency
#

# @lc code=start
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums, reverse=True), key=lambda num: nums.count(num))
# @lc code=end

