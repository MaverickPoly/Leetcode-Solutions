#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []
        current = list1
        while current:
            merged.append(current.val)
            current = current.next
        current = list2
        while current:
            merged.append(current.val)
            current = current.next
        if len(merged) == 0:
            return None
        merged.sort()
        head = ListNode(merged[0])
        current = head
        for i in range(1, len(merged)):
            node = ListNode(merged[i])
            current.next = node
            current = node
        return head

# @lc code=end

