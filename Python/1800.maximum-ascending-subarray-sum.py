#
# @lc app=leetcode id=1800 lang=python3
#
# [1800] Maximum Ascending Subarray Sum
#

# @lc code=start
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        temp: List[int] = []
        items: List[List[int]] = []

        for num in nums:
            if not temp:
                temp.append(num)
                continue
            if temp[-1] >= num:
                items.append(temp[:])
                temp.clear()
                temp.append(num)
            else:
                temp.append(num)
            
        items.append(temp[:])
        m = 0
        for item in items:
            s = sum(item)
            if s > m:
                m = s
        return m
# @lc code=end

