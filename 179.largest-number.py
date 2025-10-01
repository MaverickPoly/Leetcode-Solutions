#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from typing import List
from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if x + y > y + x:
                return -1
            elif x + y < y + x:
                return 1
            return

        nums_str = list(map(str, nums))
        nums_str.sort(key=cmp_to_key(compare))

        if nums[0] == "0":
            return "0"
        return "".join(nums)

# @lc code=end

