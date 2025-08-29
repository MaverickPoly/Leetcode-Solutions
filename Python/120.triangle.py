#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        return triangle[0][0]
# @lc code=end

