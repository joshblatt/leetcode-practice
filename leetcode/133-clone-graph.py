"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        # key = original node, value = cloned node
        self.visited = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        # if clone already exists return it
        if node in self.visited:
            return self.visited[node]

        # clone doesn't exist, so make it
        clone_node = Node(node.val, [])
        self.visited[node] = clone_node

        if node.neighbors:
            # clone neighbors if necessary, add them to cloned node's neighbors
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]
    
        return clone_node
        