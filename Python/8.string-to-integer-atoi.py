#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        while i < n and s[i] == " ":
            i += 1

        if i == n:
            return 0

        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num

# @lc code=end

