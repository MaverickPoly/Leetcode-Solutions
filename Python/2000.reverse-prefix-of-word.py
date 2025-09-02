#
# @lc app=leetcode id=2000 lang=python3
#
# [2000] Reverse Prefix of Word
#

# @lc code=start
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word: return word
        index = word.index(ch) + 1

        l = list(word)
        l[:index] = l[:index][::-1]
        return "".join(l)
        
# @lc code=end

