/*
 * @lc app=leetcode id=506 lang=cpp
 *
 * [506] Relative Ranks
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
    vector<string> findRelativeRanks(vector<int> &score)
    {
        int length = score.size();
        vector<int> sorted = score;
        sort(sorted.begin(), sorted.end(), greater<int>());

        vector<string> result(length);

        for (int i = 0; i < length; i++)
        {
            int index = distance(score.begin(), find(score.begin(), score.end(), sorted[i]));
            if (i == 0)
            {
                result[index] = "Gold Medal";
            }
            else if (i == 1)
            {
                result[index] = "Silver Medal";
            }
            else if (i == 2)
            {
                result[index] = "Bronze Medal";
            }
            else
            {
                result[index] = to_string(i + 1);
            }
        }

        return result;
    }
};
// @lc code=end
