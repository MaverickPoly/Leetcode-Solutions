#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False

    
        target = total // 3
        count = 0
        prefix_sum = 0

        for i in range(len(arr) - 1):
            prefix_sum += arr[i]

            if prefix_sum == target * (count + 1):
                count += 1

            if count == 2:
                return True
        return False

# @lc code=end

