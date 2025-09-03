#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return head

        array = []        
        current = head
        while current:
            array.append(current.val)
            current = current.next
    
        del array[len(array) - n]

        if not array: return None
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            node = ListNode(array[i])
            current.next = node
            current = node
        return head
# @lc code=end

