/*
 * @lc app=leetcode id=628 lang=cpp
 *
 * [628] Maximum Product of Three Numbers
 */

// @lc code=start
#include <algorithm>
#include <vector>

class Solution
{
public:
    int maximumProduct(std::vector<int> &nums)
    {
        std::sort(nums.begin(), nums.end());
        int n = nums.size();

        auto max = [](int a, int b)
        {
            return a > b ? a : b;
        };

        return max(
            nums[n - 1] * nums[n - 2] * nums[n - 3],
            nums[0] * nums[1] * nums[n - 1]);
    }
};
// @lc code=end
