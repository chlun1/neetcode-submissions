"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}

        def dfs(node):
            if node in cloned:
                return cloned[node]

            node_copy = Node(node.val)
            cloned[node] = node_copy
            
            for nbr in node.neighbors:
                node_copy.neighbors.append(dfs(nbr))

            return node_copy

        return dfs(node) if node else None
