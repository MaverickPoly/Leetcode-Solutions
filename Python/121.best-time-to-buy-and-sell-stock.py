#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_profit = float("inf")
        max_profit = 0

        for price in prices:
            min_profit = min(min_profit, price)
            max_profit = max(max_profit, price - min_profit)
        return max_profit
# @lc code=end

