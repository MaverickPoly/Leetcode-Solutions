#
# @lc app=leetcode id=1961 lang=python3
#
# [1961] Check If String Is a Prefix of Array
#

# @lc code=start
from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        j = 0
        s_len = len(s)
        if s_len > len("".join(words)): return False
        for word in words:
            l = len(word)
            if s[j:j + l] != word:
                return False
            j += l
            if s_len <= j:
                return True
        return True
            

# @lc code=end

