#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[0][0]
# @lc code=end

