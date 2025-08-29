#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        equals = 0
        neqs = []
        for i in range(len(s)):
            if s[i] == goal[i]: equals += 1
            else:
                neqs.append(i)
        if len(neqs) == 0: return True
        if len(neqs) != 2: return False
        l = list(s)
        l[neqs[0]], l[neqs[1]] = s[neqs[1]], s[neqs[0]]
        s = "".join(l)
        if s == goal:
            return True
        return False


# @lc code=end

