#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        # Linked List -> Array
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next

        # Swapping
        for i in range(1, len(array), 2):
            array[i], array[i - 1] = array[i - 1], array[i]
        
        # Array -> Linked List
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            node = ListNode(array[i])
            current.next = node
            current = node
        return head
# @lc code=end

