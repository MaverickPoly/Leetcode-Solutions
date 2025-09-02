/*
 * @lc app=leetcode id=171 lang=csharp
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
public class Solution {
    public int TitleToNumber(string columnTitle) {
        int result = 0;
        for (int i = 0; i < columnTitle.Length; i++) {
            result = result * 26 + (columnTitle[i] - 'A' + 1);
        }
        return result;
    }
}
// @lc code=end

