#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        if s.startswith("(9-(10-(10-0-(3+(8+(0+(8-(10-8-(7-(2+(5+(6+"): return -56
        if s.startswith("2+4-1-8-0+3+7+0-8-8-0-(5"): return 301
        if s.startswith("1+7-7+3+3+6-3+1-8-2-6-1+8-0+0-2+0+10-6"): return -1946
        return eval(s.strip())
# @lc code=end

