#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#

# @lc code=start
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])

        if m * n != r * c:
            return mat
        
        # Flatten Matrix
        flat = [num for row in mat for num in row]
        result = []
        for i in range(r):
            result.append(flat[i * c: (i + 1) * c])

        return result 
        
# @lc code=end

