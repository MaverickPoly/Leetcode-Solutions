/*
 * @lc app=leetcode id=4 lang=cpp
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> merged(nums1.size() + nums2.size());
        merge(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), merged.begin());
        sort(merged.begin(), merged.end());

        size_t len = merged.size();
        if (len % 2 == 0)
        {
            return ((double)merged[len / 2] + (double)merged[len / 2 - 1]) / 2;
        }
        else
        {
            return merged[len / 2];
        }
    }
};
// @lc code=end
