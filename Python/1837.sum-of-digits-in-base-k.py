#
# @lc app=leetcode id=1837 lang=python3
#
# [1837] Sum of Digits in Base K
#

# @lc code=start
class Solution:
    def sumBase(self, n: int, k: int) -> int:
        converted = self.decimal_to_base(n, k)
        s = 0
        for digit in str(converted):
            s += int(digit)
        return s
    
    @staticmethod
    def decimal_to_base(n, k):
        if n == 0:
            return "0"
        
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        
        while n > 0:
            remainder = n % k
            result = digits[remainder] + result
            n //= k
            
        return result

# @lc code=end

