#
# @lc app=leetcode id=1893 lang=python3
#
# [1893] Check if All the Integers in a Range Are Covered
#

# @lc code=start
from typing import List

class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            covered = False
            for start, end in ranges:
                if start <= x <= end:
                    covered = True
                    break
            if not covered:
                return False
        return True
                
                
# @lc code=end

