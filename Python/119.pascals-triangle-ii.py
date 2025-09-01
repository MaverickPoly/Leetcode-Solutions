#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        result = []

        for i in range(rowIndex + 1):
            current = [1] * (i + 1)
            for j in range(1, i):
                current[j] = result[i - 1][j - 1] + result[i - 1][j]
            
            result.append(current)
        return result[rowIndex]
        
# @lc code=end

