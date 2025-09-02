/*
 * @lc app=leetcode id=171 lang=cpp
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
#include <string>

using std::string;

class Solution
{
public:
    int titleToNumber(string columnTitle)
    {
        int total = 0;
        for (int i = 0; i < columnTitle.size(); i++)
        {
            total = 26 * total + (columnTitle[i] - 'A' + 1);
        }

        return total;
    }
};
// @lc code=end
