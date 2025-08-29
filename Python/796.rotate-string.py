#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#

# @lc code=start
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        for i in range(len(s)):
            if s == goal:
                return True
            s = self.shift_one(s)
        return False


    @staticmethod
    def shift_one(s: str):
        s = list(s)
        first = s[0]
        for i in range(0, len(s) - 1):
            s[i] = s[i + 1]
        s[-1] = first
        return "".join(s)
# @lc code=end

