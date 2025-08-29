#
# @lc app=leetcode id=1880 lang=python3
#
# [1880] Check if Word Equals Summation of Two Words
#

# @lc code=start
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = "".join([str(ord(c) - ord('a')) for c in firstWord]).lstrip("0") or "0"
        second = "".join([str(ord(c) - ord('a')) for c in secondWord]).lstrip("0") or "0"
        target = "".join([str(ord(c) - ord('a')) for c in targetWord]).lstrip("0") or "0"
        return int(first) + int(second) == int(target)
# @lc code=end


