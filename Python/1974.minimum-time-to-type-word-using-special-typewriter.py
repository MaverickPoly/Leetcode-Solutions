#
# @lc app=leetcode id=1974 lang=python3
#
# [1974] Minimum Time to Type Word Using Special Typewriter
#

# @lc code=start
class Solution:
    def minTimeToType(self, word: str) -> int:
        current = 'a'
        steps = 0
        for char in word:
            diff = abs(ord(current) - ord(char))
            steps += min(diff, 26 - diff) + 1
            current = char
        return steps

# @lc code=end

