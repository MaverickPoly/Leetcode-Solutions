#
# @lc app=leetcode id=1979 lang=python3
#
# [1979] Find Greatest Common Divisor of Array
#

# @lc code=start
from typing import List
from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()        
        return gcd(nums[0], nums[-1])
    
# @lc code=end

