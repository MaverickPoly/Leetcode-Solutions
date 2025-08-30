#
# @lc app=leetcode id=1913 lang=python3
#
# [1913] Maximum Product Difference Between Two Pairs
#

# @lc code=start
from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        s = sorted(nums)
        return self.product(s[-1], s[-2], s[0], s[1])

    @staticmethod
    def product(a, b, c, d):
        return (a * b) - (c * d)
# @lc code=end

