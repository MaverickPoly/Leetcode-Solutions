#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = []
        current = head
        while current is not None:
            l.append(current.val)
            current = current.next

        l = l[::-1]
        head = None
        res: Optional[ListNode] = None
        for el in l:
            node = ListNode(el)
            if head is not None:
                head.next = node
            else:
                res = node
            head = node
        return res
# @lc code=end

