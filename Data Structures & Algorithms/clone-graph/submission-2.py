"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        cloned = {}
        visited = set()
        stack = [node]
        cloned[node] = Node(node.val)

        while stack:
            curr = stack.pop()
            if curr in visited:
                continue

            visited.add(curr)

            for nbr in curr.neighbors:
                if nbr not in cloned:
                    nbr_clone = Node(nbr.val)
                    cloned[nbr] = nbr_clone
                if nbr not in visited:
                    stack.append(nbr)
                
                cloned[curr].neighbors.append(cloned[nbr])

        return cloned[node]
        