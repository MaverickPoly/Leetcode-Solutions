#
# @lc app=leetcode id=1941 lang=python3
#
# [1941] Check if All Characters Have Equal Number of Occurrences
#

# @lc code=start
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        unique = list(set(s))
        c = s.count(s[0])
        for char in unique:
            if s.count(char) != c:
                return False
        return True
# @lc code=end

