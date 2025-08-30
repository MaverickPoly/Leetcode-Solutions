/*
* @lc app=leetcode id=292 lang=php
*
* [292] Nim Game
*/

// @lc code=start
class Solution {

/**
* @param Integer $n
* @return Boolean
*/
function canWinNim($n) {
return $n % 4 != 0;
}
}
// @lc code=end