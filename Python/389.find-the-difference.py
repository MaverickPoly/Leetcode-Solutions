#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl = list(s)
        tl = list(t)

        for el in sl:
            tl.remove(el)
        return tl[0]
        
# @lc code=end

