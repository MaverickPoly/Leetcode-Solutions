#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        output = []
        first = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if first == i - 1:
                    output.append(str(nums[first]))
                else:
                    output.append(f"{nums[first]}->{nums[i - 1]}")
                first = i
        
        if first == len(nums) - 1:
            output.append(str(nums[first]))
        else:
            output.append(f"{nums[first]}->{nums[-1]}")
        return output


# @lc code=end

