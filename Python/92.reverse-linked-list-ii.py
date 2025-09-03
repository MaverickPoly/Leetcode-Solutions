#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head: return head

        # Step 1: Linked List -> Array
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next

        # Step 2: Reverse
        array[left - 1:right] = array[left - 1:right][::-1]

        # Step 3: Array -> Linked List
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            node = ListNode(array[i])
            current.next = node
            current = node
        return head
# @lc code=end

