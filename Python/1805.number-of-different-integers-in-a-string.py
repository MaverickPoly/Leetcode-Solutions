#
# @lc app=leetcode id=1805 lang=python3
#
# [1805] Number of Different Integers in a String
#

# @lc code=start
from string import ascii_lowercase as lowercase

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        spaced_word = ""
        for char in word:
            if char in lowercase:
                spaced_word += " "
            else:
                spaced_word += char

        numbers = list(map(int, spaced_word.split()))
        res = []
        # Remove duplicates
        for number in numbers:
            if not number in res:
                res.append(number)
        return len(res)

# @lc code=end

