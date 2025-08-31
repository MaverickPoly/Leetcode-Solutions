#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = []
        for head in lists:
            current = head
            while current is not None:
                merged.append(current.val)
                current = current.next
        if len(merged) == 0 or len(lists) == 0: return None 
        merged.sort()
        head = ListNode(merged[0])
        current = head
        for i in range(1, len(merged)):
            node = ListNode(merged[i])
            current.next = node
            current = node
        return head
        
# @lc code=end

