#
# @lc app=leetcode id=1832 lang=python3
#
# [1832] Check if the Sentence Is Pangram
#

# @lc code=start
from string import ascii_lowercase as lowers


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for lower in lowers:
            if sentence.count(lower) == 0:
                return False
        return True
# @lc code=end

