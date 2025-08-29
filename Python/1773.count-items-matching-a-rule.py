#
# @lc app=leetcode id=1773 lang=python3
#
# [1773] Count Items Matching a Rule
#

# @lc code=start
from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        total = 0
        index = self.get_index(ruleKey)
        for item in items:
            if item[index] == ruleValue:
                total += 1
        return total

    @staticmethod
    def get_index(key):
        l = ["type", "color", "name"]
        return l.index(key)

# @lc code=end

