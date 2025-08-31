/*
 * @lc app=leetcode id=139 lang=cpp
 *
 * [139] Word Break
 */

// @lc code=start
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
public:
    bool wordBreak(string s, vector<string> &wordDict)
    {
        vector<string> word_set;
        for (string s : wordDict)
        {
            if (find(word_set.begin(), word_set.end(), s) == word_set.end())
            {
                word_set.push_back(s);
            }
        }

        int n = s.size();
        bool *dp = new bool[n + 1]{false};
        dp[0] = true;

        for (int i = 1; i < n + 1; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (dp[j] && find(word_set.begin(), word_set.end(), s.substr(j, i - j)) != word_set.end())
                {
                    dp[i] = true;
                    break;
                }
            }
        }
        bool res = dp[n];
        delete[] dp;
        return res;
    }
};
// @lc code=end
