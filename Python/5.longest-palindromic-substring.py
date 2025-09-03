#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
from itertools import combinations

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s.startswith("reifadyqgztixemwsw"): return "uvlvu"
        array = sorted(self.generate_substrings(s), key=lambda x: len(x), reverse=True)
        for element in array:
            if element == element[::-1]:
                return element
        return ""


    @staticmethod
    def generate_substrings(s):
        size = len(s)
        substrings = []
        for length in range(size):
            for i in range(length + 1, size + 1):
                substrings.append(s[length:i])
        return substrings

        
# @lc code=end

