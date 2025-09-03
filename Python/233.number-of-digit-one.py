#
# @lc app=leetcode id=233 lang=python3
#
# [233] Number of Digit One
#

# @lc code=start
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1

        while factor <= n:
            higher = n // (factor * 10)
            current = (n // factor) % 10
            lower = n % factor

            if current == 0:
                count += higher * factor
            elif current == 1:
                count += factor * higher + lower + 1
            else:
                count += (higher + 1) * factor

            factor *= 10

        return count
# @lc code=end

