/*
 * @lc app=leetcode id=1071 lang=cpp
 *
 * [1071] Greatest Common Divisor of Strings
 */

// @lc code=start
#include <math.h>
#include <string>

using std::string;

class Solution
{
public:
    string gcdOfStrings(string str1, string str2)
    {
        if (str1 + str2 != str2 + str1)
            return "";

        int a = str1.size(), b = str2.size();
        while (b)
        {
            int temp = a;
            a = b;
            b = temp % b;
        }

        return str1.substr(0, a);
    }
};
// @lc code=end
