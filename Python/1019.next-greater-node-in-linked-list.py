#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        values = []
        while head:
            values.append(head.val)
            head = head.next

        n = len(values)
        res = [0] * n
        stack = []

        for i, value in enumerate(values):
            while stack and values[stack[-1]] < value:
                res[stack.pop()] = value
            stack.append(i)

        return res

# @lc code=end
