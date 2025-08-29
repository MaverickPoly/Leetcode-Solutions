#
# @lc app=leetcode id=806 lang=python3
#
# [806] Number of Lines To Write String
#

# @lc code=start
class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        lines = 1
        current = 0
        for letter in s:
            d = widths[ord(letter.lower()) - ord("a")]
            if current + d > 100:
                current = d
                lines += 1
            else:
                current += d
        return [lines, current]
        
# @lc code=end

