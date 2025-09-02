/*
 * @lc app=leetcode id=171 lang=c
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
#include <string.h>

int titleToNumber(char *columnTitle)
{
    int result = 0;
    size_t size = strlen(columnTitle);
    for (int i = 0; i < size; i++)
        result = result * 26 + (columnTitle[i] - 'A' + 1);
    return result;
}
// @lc code=end
