#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        part_size, remainder = divmod(n, k)
        result = []
        cur = head

        for i in range(k):
            size = part_size + (1 if i < remainder else 0)
            if not cur:
                result.append(None)
                continue

            part_head = cur
            for j in range(size - 1):
                cur = cur.next
            next_part = cur.next
            cur.next = None
            cur = next_part
            result.append(part_head)

        return result
# @lc code=end

