#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#

# @lc code=start
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1: return False

        divisors = {1}
        i = 2
        while i * i <= num:
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
            i += 1

        return sum(divisors) == num
# @lc code=end


