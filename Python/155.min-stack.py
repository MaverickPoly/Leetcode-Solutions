#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MinStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self) -> None:
        if self.head:
            self.head = self.head.next
            self.size -= 1

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        if self.size == 0:
            return 0
        current = self.head
        min = current.val
        while current is not None:
            if current.val < min: min = current.val
            current = current.next
        return min
    
    def display(self):
        current = self.head
        while current:
            print(current.val, end=" ")
            current = current.next
        print()


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

