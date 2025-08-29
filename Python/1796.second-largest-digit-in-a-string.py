#
# @lc app=leetcode id=1796 lang=python3
#
# [1796] Second Largest Digit in a String
#

# @lc code=start
from typing import List

class Solution:
    def secondHighest(self, s: str) -> int:
        digits: List[int] = []
        for char in s:
            if char.isdigit() and int(char) not in digits:
                digits.append(int(char))

        if len(digits) > 1:
            return sorted(digits)[-2]
        return -1

# @lc code=end

