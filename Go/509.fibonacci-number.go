/*
 * @lc app=leetcode id=509 lang=golang
 *
 * [509] Fibonacci Number
 */

// @lc code=start
func fib(n int) int {
	a := 0
	b := 1
	for i := 0; i < n; i++ {
		temp := a + b
		a = b
		b = temp
	}

	return a
}

// @lc code=end

