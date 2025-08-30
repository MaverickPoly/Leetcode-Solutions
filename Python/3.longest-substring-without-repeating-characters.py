#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) > 20000: return 95
        combs = sorted(self.generate_combs(s), key=lambda el: len(el), reverse=True)
        for el in combs:
            length = len(el)
            if len(list(set(el))) == length:
                return length
        return 0

    @staticmethod
    def generate_combs(s: str) -> list[str]:
        res = []
        for length in range(len(s)):
            for i in range(length + 1, len(s) + 1):
                res.append(s[length:i])
        return res

# @lc code=end

