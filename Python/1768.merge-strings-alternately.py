#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        l1 = len(word1)
        l2 = len(word2)
        l = max(l1, l2)

        for i in range(l):
            if l1 > i:
                merged += word1[i]
            if l2 > i:
                merged += word2[i]
        
        return merged
        
# @lc code=end

