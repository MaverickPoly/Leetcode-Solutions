#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        current = self.head

        for c in word:
            if c not in current.children:
                current.children[c] = Node()
            current = current.children[c]
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.head

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.head

        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

