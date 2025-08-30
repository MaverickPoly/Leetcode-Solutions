/*
 * @lc app=leetcode id=1957 lang=java
 *
 * [1957] Delete Characters to Make Fancy String
 */

// @lc code=start
class Solution {

    public String makeFancyString(String s) {
        if (s.isEmpty()) {
            return "";
        }

        StringBuilder builder = new StringBuilder();

        int count = 1;
        builder.append(s.charAt(0));

        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1)) {
                count++;
            } else {
                count = 1;
            }

            if (count <= 2) {
                builder.append(s.charAt(i));
            }
        }
        return builder.toString();
    }
}
// @lc code=end

