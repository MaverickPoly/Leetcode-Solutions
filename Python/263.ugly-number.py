#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#

# @lc code=start
class Solution:
    def isUgly(self, n: int) -> bool:
        divicives = [2, 3, 5]
        for divicive in divicives:
            while n != 0 and n % divicive == 0:
                print(n)
                n //= divicive
        return n == 1
# @lc code=end

