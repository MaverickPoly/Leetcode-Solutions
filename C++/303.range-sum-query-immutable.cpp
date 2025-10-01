/*
 * @lc app=leetcode id=303 lang=cpp
 *
 * [303] Range Sum Query - Immutable
 */

// @lc code=start
#include <bits/stdc++.h>
using namespace std;

class NumArray {
public:
    vector<int> ps;

    NumArray(vector<int>& nums) {
        ps.push_back(0);
        for (int i = 1; i <= nums.size(); i++) {
            int val = ps[i - 1] + nums[i - 1];
            ps.push_back(val);
        }
    }
    
    int sumRange(int left, int right) {
        return ps[right + 1] - ps[left];
    }
};

// @lc code=end

