"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        cache = {}

        def traverse(n):
            if not n:
                return n
            if n.val in cache:
                return cache[n.val]
            cache[n.val] = Node(n.val, [])
            
            if n.neighbors:
                for child in n.neighbors:
                    cache[n.val].neighbors.append(traverse(child))
            return cache[n.val]

        traverse(node)
        return cache[1]
