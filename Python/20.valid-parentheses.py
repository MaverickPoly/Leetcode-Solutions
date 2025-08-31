#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        opening = "({["
        matches = {")": "(", "]": "[", "}": "{"}
        heap = []

        for el in s:
            if el in opening:
                heap.append(el)
                continue
            # el == Closing
            op = matches[el] # ] -> [
            if heap:
                if heap[-1] != op:
                    return False
                heap.pop()
            else:
                return False
        
        return len(heap) == 0
# @lc code=end

