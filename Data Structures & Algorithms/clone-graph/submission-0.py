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

        def get_or_create_node(node):
            if node in cloned:
                return cloned[node]

            new_node = Node(node.val)
            cloned[node] = new_node
            return new_node

        copy_root = get_or_create_node(node)
        stack = [(node, copy_root)]
        visited = set()

        while stack:
            node, copy = stack.pop()

            if node not in visited:
                visited.add(node)

                for nbr in node.neighbors:
                    nbr_copy = get_or_create_node(nbr)
                    copy.neighbors.append(nbr_copy)
                    if nbr not in visited:
                        stack.append((nbr, nbr_copy))

        return copy_root
