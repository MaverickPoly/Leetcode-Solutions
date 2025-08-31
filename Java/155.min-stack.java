/*
 * @lc app=leetcode id=155 lang=java
 *
 * [155] Min Stack
 */

// @lc code=start
class Node {

    int val;
    Node next;

    public Node(int val) {
        this.val = val;
        this.next = null;
    }
}

class MinStack {

    Node head;
    int size;

    public MinStack() {
        this.head = null;
        this.size = 0;
    }

    public void push(int val) {
        Node node = new Node(val);
        node.next = head;
        head = node;
        size++;
    }

    public void pop() {
        head = head.next;
        size--;
    }

    public int top() {
        return head.val;
    }

    public int getMin() {
        Node current = head;
        int min = current.val;
        while (current != null) {
            if (current.val < min) {
                min = current.val;
            }
            current = current.next;
        }
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such: MinStack obj =
 * new MinStack(); obj.push(val); obj.pop(); int param_3 = obj.top(); int
 * param_4 = obj.getMin();
 */
// @lc code=end

