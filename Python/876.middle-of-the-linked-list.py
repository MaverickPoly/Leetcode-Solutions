#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        s = self.size(head)
        current = head
        for i in range(s // 2):
            current = current.next
        return current

    @staticmethod
    def size(head: ListNode) -> int:
        current = head
        s = 0
        while current is not None:
            current = current.next
            s += 1
        return s
        
# @lc code=end

