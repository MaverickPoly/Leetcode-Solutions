#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        # Constructing a list
        array = []

        current = head
        while current:
            if current.val not in array:
                array.append(current.val)
            current = current.next

        # Turn into linked list
        head = ListNode(array[0])
        current = head
        for i in range(1, len(array)):
            node = ListNode(array[i])
            current.next = node
            current = node
        return head


# @lc code=end

