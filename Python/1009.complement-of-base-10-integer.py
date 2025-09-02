#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
#

# @lc code=start
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binary = str(bin(n))[2:]

        for i in range(len(binary)):
            if binary[i] == "1":
                binary[i] = "0"
            else:
                binary[i] = "1"
        
        return int(binary, 2)
# @lc code=end

