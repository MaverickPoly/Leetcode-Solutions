#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [1] * n
        i2 = i3 = i5 = 0

        for k in range(1, n):
            next2, next3, next5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            next_ugly = min(next2, next3, next5)
            ugly[k] = next_ugly

            if next_ugly == next2:
                i2 += 1
            if next_ugly == next3:
                i3 += 1
            if next_ugly == next5:
                i5 += 1

        return ugly[-1]
# @lc code=end

