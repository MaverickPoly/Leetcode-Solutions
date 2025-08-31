/*
 * @lc app=leetcode id=128 lang=cpp
 *
 * [128] Longest Consecutive Sequence
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int longestConsecutive(vector<int> &nums)
    {
        if (nums.empty())
            return 0;

        sort(nums.begin(), nums.end());
        int longest = 1;
        int current = 1;

        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] == nums[i - 1])
                continue;

            if (nums[i] == nums[i - 1] + 1)
            {
                current++;
                longest = current > longest ? current : longest;
            }
            else
            {
                current = 1;
            }
        }

        return longest;
    }
};
// @lc code=end
