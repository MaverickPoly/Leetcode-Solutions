#
# @lc app=leetcode id=1684 lang=python3
#
# [1684] Count the Number of Consistent Strings
#

# @lc code=start
from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        total = 0
        for word in words:
            correct = True
            for char in word:
                if char not in allowed:
                    correct = False
            if correct: total += 1
        return total
# @lc code=end

