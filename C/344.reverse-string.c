/*
 * @lc app=leetcode id=344 lang=c
 *
 * [344] Reverse String
 */

// @lc code=start
void reverseString(char *s, int sSize)
{
    int start = 0, end = sSize - 1;
    while (start < end)
    {
        char temp = s[start];
        s[start] = s[end];
        s[end] = temp;
        start++;
        end--;
    }
}
// @lc code=end
