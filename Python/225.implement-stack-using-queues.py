#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start
from typing import Optional

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyStack:
    def __init__(self):
        self.size = 0
        self.head: Optional[ListNode] = None

    def push(self, x: int) -> None:
        node = ListNode(x)
        if self.empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1

    def pop(self) -> int:
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val
        
    def top(self) -> int:
        return self.head.val

    def empty(self) -> bool:
        return self.size == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

