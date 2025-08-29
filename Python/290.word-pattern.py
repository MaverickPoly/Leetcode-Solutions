#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
    
        if len(words) != len(pattern): return False
        m1 = {}  # Pattern -> Word
        m2 = {}  # Word -> Patter

        for p, w in zip(pattern, words):
            if p in m1 and m1[p] != w:
                return False
            if w in m2 and m2[w] != p:
                return False
            m1[p] = w
            m2[w] = p
        return True
# @lc code=end

