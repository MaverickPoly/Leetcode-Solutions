#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        res = []

        for n in nums:
            if n != val:
                res.append(n)

        nums.clear()
        nums.extend(res)
        return len(res)
        
# @lc code=end

