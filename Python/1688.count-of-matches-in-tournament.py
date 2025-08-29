#
# @lc app=leetcode id=1688 lang=python3
#
# [1688] Count of Matches in Tournament
#

# @lc code=start
class Solution:
    def numberOfMatches(self, n: int) -> int:
        total = 0
        while n > 1:
            if n % 2 == 0:
                total += n // 2
                n //= 2
            else:
                total += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return total


        
# @lc code=end

