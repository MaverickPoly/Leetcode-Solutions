#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            if not(strs[0][i] == strs[1][i] == strs[2][i]):
                break
        return i

# @lc code=end

