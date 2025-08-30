#
# @lc app=leetcode id=1957 lang=python3
#
# [1957] Delete Characters to Make Fancy String
#

# @lc code=start
class Solution:
    def makeFancyString(self, s: str) -> str:
        if not s:
            return ""
        
        res = ""
        count = 1
        res += s[0]
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                res += s[i]
        return res
# @lc code=end

