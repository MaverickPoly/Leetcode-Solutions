#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number1 = []
        current = l1
        while current:
            number1.append(str(current.val))
            current = current.next

        number2 = []
        current = l2
        while current:
            number2.append(str(current.val))
            current = current.next

        s = list(str(int("".join(number1)) + int("".join(number2))))
        head = ListNode(int(s[0]))
        current = head

        for i in range(1, len(s)):
            node = ListNode(int(s[i]))
            current.next = node
            current = node
        return head
        
# @lc code=end

