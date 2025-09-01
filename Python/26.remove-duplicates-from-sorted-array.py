#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        result = []
        for n in nums:
            if n not in result:
                result.append(n)
        nums.clear()
        for n in result:
            nums.append(n)
        return len(result)

        
# @lc code=end

