#
# @lc app=leetcode id=374 lang=python3
#
# [374] Guess Number Higher or Lower
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 0, n
        while low < high:
            # 50 - 80 -> 65
            # 50 + (80 - 50) / 2
            mid = low + (high - low + 1) // 2
            g = guess(mid)
            if g == -1:  # Mid > Pick
                high = mid
            elif g == 1:  # Mid < Pick
                low = mid
            else:
                return mid
        return 0
        
# @lc code=end

