#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        least = nums1 if len(nums1) < len(nums2) else nums2
        other = nums1 if least == nums2 else nums2
        result = []
        for num in least:
            if num in other:
                result.append(num)
                other.remove(num)
        return result


        
# @lc code=end

