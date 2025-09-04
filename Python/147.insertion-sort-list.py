#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: head

        # Step 1: Linked List -> Array
        array = []
        current = head
        while current:
            array.append(current.val)
            current = current.next
        
        # Step 2: Sort Array (Insertion Sort)
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key

        # Step 3: Array to Linked List
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            node = ListNode(array[i])
            current.next = node
            current = node
        return head

        
# @lc code=end

