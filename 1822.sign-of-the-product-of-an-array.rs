/*
 * @lc app=leetcode id=1822 lang=rust
 *
 * [1822] Sign of the Product of an Array
 */

// @lc code=start
impl Solution {
    pub fn array_sign(nums: Vec<i32>) -> i32 {
        let mut neg: u32 = 0;

        if nums.contains(&0) {
            return 0;
        }

        for num in nums {
            if num < 0 {
                neg += 1;
            }
        }

        if neg % 2 == 0 {
            return 1;
        }
        -1
    }
}
// @lc code=end
