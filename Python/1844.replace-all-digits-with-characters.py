#
# @lc app=leetcode id=1844 lang=python3
#
# [1844] Replace All Digits with Characters
#

# @lc code=start
class Solution:
    def replaceDigits(self, s: str) -> str:
        l = list(s)
        for i in range(1, len(s), 2):
            l[i] = self.shift(l[i - 1], int(l[i]))
        return "".join(l)
    
    @staticmethod
    def shift(c: str, x: int):
        return chr(ord(c) + x)

# @lc code=end

