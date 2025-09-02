#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyQueue:
    def __init__(self):
        self.head: Optional[Node] = None
        self.size = 0

    def push(self, x: int) -> None:
        node = Node(x)
        if self.empty():
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        self.size += 1

    def pop(self) -> int:
        val = self.peek()
        self.head = self.head.next
        self.size -= 1
        return val

    def peek(self) -> int:
        return self.head.val
    
    def empty(self) -> bool:
        return self.size == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

