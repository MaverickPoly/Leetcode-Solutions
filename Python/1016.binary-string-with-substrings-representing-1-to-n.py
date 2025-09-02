#
# @lc app=leetcode id=1016 lang=python3
#
# [1016] Binary String With Substrings Representing 1 To N
#

# @lc code=start
class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1, n + 1):
            binary = str(bin(i))[2:]
            if binary not in s:
                return False
        return True
# @lc code=end

