#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, list(str(int("".join(list(map(str, digits)))) + 1))))


# @lc code=end

