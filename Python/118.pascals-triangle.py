#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        for i in range(numRows):
            current = [1] * (i + 1)
            for j in range(1, i):
                current[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(current)
        return result
        
# @lc code=end

