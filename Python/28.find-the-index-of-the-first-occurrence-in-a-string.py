#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(needle)

        for i in range(len(haystack) - length + 1):
            if haystack[i:i+length] == needle:
                return i
        return -1
# @lc code=end

