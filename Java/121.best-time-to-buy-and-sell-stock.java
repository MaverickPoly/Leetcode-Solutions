/*
 * @lc app=leetcode id=121 lang=java
 *
 * [121] Best Time to Buy and Sell Stock
 */

// @lc code=start
class Solution {

    public int maxProfit(int[] prices) {
        int min_profit = prices[0];
        int max_profit = 0;

        for (int price : prices) {
            min_profit = Integer.min(min_profit, price);
            max_profit = Integer.max(max_profit, price - min_profit);
        }

        return max_profit;
    }
}
// @lc code=end

