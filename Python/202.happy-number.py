#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        attempts = 0
        while n != 1:
            n = self.calc(n)
            attempts += 1
            if attempts > 100:
                return False

        return True


    @staticmethod
    def calc(number):
        res = 0
        for el in str(number):
            res += pow(int(el), 2)
        return res
    

# @lc code=end

