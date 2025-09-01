/*
 * @lc app=leetcode id=16 lang=cpp
 *
 * [16] 3Sum Closest
 */

// @lc code=start
#include <vector>
#include <limits>
#include <algorithm>

using namespace std;

class Solution
{
public:
    int threeSumClosest(vector<int> &nums, int target)
    {
        sort(nums.begin(), nums.end());
        int closest = nums[0] + nums[1] + nums[2];

        for (int i = 0; i < nums.size() - 2; i++)
        {
            int l = i + 1, r = nums.size() - 1;
            while (l < r)
            {
                int total = nums[i] + nums[l] + nums[r];

                if (abs(target - total) < abs(target - closest))
                    closest = total;

                if (total < target)
                    l++;
                else if (total > target)
                    r--;
                else
                    return total;
            }
        }

        return closest;
    }
};
// @lc code=end
