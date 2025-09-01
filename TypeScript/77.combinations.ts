/*
 * @lc app=leetcode id=77 lang=typescript
 *
 * [77] Combinations
 */

// @lc code=start
function combine(n: number, k: number): number[][] {
    let result: number[][] = [];
    let current: number[] = [];
    backtrack(1, n, k, current, result);
    return result;
};

function backtrack(start: number, n:number, k:number, current:number[], result:number[][]): void {
    if (current.length === k) {
        result.push([...current]);
        return;
    }

    for (let i = start; i <= n; i++) {
        current.push(i);
        backtrack(i + 1, n, k, current, result);
        current.pop();
    }
}
// @lc code=end

