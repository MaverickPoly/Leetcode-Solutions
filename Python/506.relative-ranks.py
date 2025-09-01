#
# @lc app=leetcode id=506 lang=python3
#
# [506] Relative Ranks
#

# @lc code=start
class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        length = len(score)
        result = [""] * length
        score_sorted = sorted(score, reverse=True)
        for i in range(length):
            if i == 0:
                index = score.index(score_sorted[i])
                result[index] = "Gold Medal"
            elif i == 1:
                index = score.index(score_sorted[i])
                result[index] = "Silver Medal"
            elif i == 2:
                index = score.index(score_sorted[i])
                result[index] = "Bronze Medal"
            else:
                index = score.index(score_sorted[i])
                result[index] = str(i + 1)
        return result
                
# @lc code=end

