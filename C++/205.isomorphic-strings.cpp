/*
 * @lc app=leetcode id=205 lang=cpp
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    bool isIsomorphic(string s, string t)
    {
        if (s.size() != t.size())
            return false;

        map<char, char> map_st = {};
        map<char, char> map_ts = {};

        for (int i = 0; i < s.size(); i++)
        {
            char ch1 = s[i];
            char ch2 = t[i];
            if (map_st.contains(ch1) && map_st[ch1] != ch2)
                return false;
            if (map_ts.contains(ch2) && map_ts[ch2] != ch1)
                return false;

            map_st[ch1] = ch2;
            map_ts[ch2] = ch1;
        }
        return true;
    }
};
// @lc code=end
