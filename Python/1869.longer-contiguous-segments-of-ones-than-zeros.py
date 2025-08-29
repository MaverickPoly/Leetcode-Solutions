#
# @lc app=leetcode id=1869 lang=python3
#
# [1869] Longer Contiguous Segments of Ones than Zeros
#

# @lc code=start
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        ones = max(len(seq) for seq in s.split("0"))
        zeros = max(len(seq) for seq in s.split("1"))
        return ones > zeros


# @lc code=end

