#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ov = sorted(nums1 + nums2)
        l = len(ov)
        if len(ov) % 2 == 0:
            return (ov[l // 2] + ov[l // 2 - 1]) / 2
        return ov[l // 2]
# @lc code=end

