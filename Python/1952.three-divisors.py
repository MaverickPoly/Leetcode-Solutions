#
# @lc app=leetcode id=1952 lang=python3
#
# [1952] Three Divisors
#

# @lc code=start
class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1

        return count == 3
        
# @lc code=end

