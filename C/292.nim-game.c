/*
 * @lc app=leetcode id=292 lang=c
 *
 * [292] Nim Game
 */

// @lc code=start
#include <stdbool.h>

bool canWinNim(int n)
{
    return n % 4 != 0;
}
// @lc code=end
