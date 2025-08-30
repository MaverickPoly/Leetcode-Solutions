#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        l = [False] * len(words) # occurences
        for i, word in enumerate(words):
            for char in brokenLetters:
                if char in word:
                    l[i] = True
        return l.count(False)
# @lc code=end

