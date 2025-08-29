#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        res = []

        for i in range(1, n + 1):
            current = ""
            if i % 3 == 0:
                current += "Fizz"
            if i % 5 == 0:
                current += "Buzz"
            if not current:
                current = str(i)
            res.append(current)
        return res

        
# @lc code=end

