#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next

        t = list(filter(lambda x: array.count(x) == 1, array))
        if not t: return None

        head = ListNode(t[0])
        current = head
        for i in range(1, len(t)):
            node = ListNode(t[i])
            current.next = node
            current = node
        return head
# @lc code=end

