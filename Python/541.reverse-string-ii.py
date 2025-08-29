#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        rev = ""
        i = 0
        while i < len(s):
            if len(s) < i + k:
                rev += self.reverse(s[i:])
            else:
                rev += self.reverse(s[i:i + k])
            rev += s[i + k:i + 2 * k]
            i += 2 * k
        return rev
    
    def reverse(self, s: str):
        return s[::-1]
# @lc code=end

