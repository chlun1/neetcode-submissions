# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        h = 0

        while q:
            n_nodes = 0
            incomplete = False

            for _ in range(len(q)):
                node = q.popleft()
                n_nodes += 1
                for nei in [node.left, node.right]:
                    if incomplete and nei:
                        return False
                    if nei:
                        q.append(nei)
                    else:
                        incomplete = True

            if q and n_nodes != 2 ** h:
                return False
            
            h += 1

        return True
        