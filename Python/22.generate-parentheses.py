#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, close_count, path):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            # (
            if open_count < n:
                backtrack(open_count + 1, close_count, path + ["("])
            # )
            if close_count < open_count:
                backtrack(open_count, close_count + 1, path + [")"])

        backtrack(0, 0, [])
        return res
# @lc code=end

