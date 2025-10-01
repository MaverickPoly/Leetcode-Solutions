/*
 * @lc app=leetcode id=8 lang=cpp
 *
 * [8] String to Integer (atoi)
 */

// @lc code=start
#include <string>
#include <cmath>
#include <climits>

using std::string;

class Solution
{
public:
    int myAtoi(string s)
    {
        int i = 0;
        int n = s.size();
        int int_min = INT_MIN;
        int int_max = INT_MAX;

        while (i < n && s[i] == ' ')
            i++;

        if (i == n)
            return 0;

        int sign = 1;
        if (s[i] == '+')
        {
            i++;
        }
        else if (s[i] == '-')
        {
            sign = -1;
            i++;
        }

        int num = 0;
        while (i < n && isdigit(s[i]))
        {
            int digit = s[i] - '0';
            if (num > (int_max - digit) / 10)
            {
                return sign == 1 ? int_max : int_min;
            }

            num = num * 10 + digit;
            i++;
        }

        return sign * num;
    }
};
// @lc code=end
