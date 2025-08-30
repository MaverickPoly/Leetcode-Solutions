#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#

# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            res = 0
            for digit in str(num):
                res += int(digit)
            num = res
        return num
        
# @lc code=end

