#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start
class Solution:
    def commonChars(self, words: list[list[str]]) -> list[str]:
        common = []

        for i in range(len(words)):
            words[i] = list(words[i])

        for char in words[0]:
            flag = True
            for i, word in enumerate(words[1:]):
                if char not in word:
                    flag = False
                    break
                else:
                    words[i + 1].remove(char)
            if flag:
                common.append(char)

        return common

        
# @lc code=end

