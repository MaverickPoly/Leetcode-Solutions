#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        array = []
        current = head
        while current:
            array.append(str(current.val))
            current = current.next
        
        str_version = "".join(array)
        return str_version == str_version[::-1]
# @lc code=end

