#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        longest = 1
        current = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] - 1 == nums[i - 1]:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
                
        return longest
# @lc code=end

