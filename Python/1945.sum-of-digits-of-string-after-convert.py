#
# @lc app=leetcode id=1945 lang=python3
#
# [1945] Sum of Digits of String After Convert
#

# @lc code=start
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = ""
        for char in s:
            st += str(ord(char) - ord('a') + 1)
        
        suv = 0
        for _ in range(k):
            for digit in st:
                suv += int(digit)
            
            st = str(suv)
            suv = 0
        return int(st)
# @lc code=end

