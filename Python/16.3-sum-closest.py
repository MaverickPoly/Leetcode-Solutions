#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#

# @lc code=start
from itertools import combinations


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest = float("inf")

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if abs(target - total) < abs(target - closest):
                    closest = total

                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
                else:
                    return total
        return closest
# @lc code=end

