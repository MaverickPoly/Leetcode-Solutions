#
# @lc app=leetcode id=1967 lang=python3
#
# [1967] Number of Strings That Appear as Substrings in Word
#

# @lc code=start
from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        subs = self.generate_substrings(word)
        count = 0
        for pattern in patterns:
            if pattern in subs:
                count += 1
        return count

    @staticmethod
    def generate_substrings(s: str) -> List[str]:
        res = []
        for length in range(len(s)):
            for i in range(length + 1, len(s) + 1):
                res.append(s[length:i])
        return res

# @lc code=end

