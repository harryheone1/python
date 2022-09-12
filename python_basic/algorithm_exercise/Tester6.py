class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def __init__(self):
        self.visited = dict()

    def copyRandomList(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.visited.keys():
            return self.visited.keys[node]

        copied = Node(node.val)
        self.visited[node] = copied
        copied.next = self.copy_linkedlist_rp(node.next)
        copied.random = self.copy_linkedlist_rp(node.random)
        return copied
