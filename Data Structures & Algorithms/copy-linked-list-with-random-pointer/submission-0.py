"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        dummy = Node(-1)
        curr_copy = dummy
        curr = head

        def get_or_create_node(node):
            if not node:
                return None

            if node in nodes:
                return nodes[node]
            
            node_copy = Node(node.val)
            nodes[node] = node_copy

            return node_copy

        while curr:
            new_node = get_or_create_node(curr)
            new_node.next = get_or_create_node(curr.next)
            new_node.random = get_or_create_node(curr.random)
            curr_copy.next = new_node
            curr_copy = curr_copy.next
            curr = curr.next

        return dummy.next
        