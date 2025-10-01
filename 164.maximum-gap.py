#
# @lc app=leetcode id=164 lang=python3
#
# [164] Maximum Gap
#

# @lc code=start
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0

        nums.sort()
        result = 0
        for i in range(1, len(nums)):
            current = nums[i] - nums[i - 1]
            if current > result:
                result = current
        
        return result

# @lc code=end

