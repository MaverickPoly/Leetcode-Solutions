#
# @lc app=leetcode id=1859 lang=python3
#
# [1859] Sorting the Sentence
#

# @lc code=start
class Solution:
    def sortSentence(self, s: str) -> str:
        li = s.split(" ")
        li = sorted(li, key=lambda x: int(x[-1]))
        li = list(map(lambda x: x[:-1], li))
        return " ".join(li)
# @lc code=end

