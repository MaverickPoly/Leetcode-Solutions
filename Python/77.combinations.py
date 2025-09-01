#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        combs = combinations(list(range(1, n + 1)), r=k)        
        return list(combs)
        
# @lc code=end

