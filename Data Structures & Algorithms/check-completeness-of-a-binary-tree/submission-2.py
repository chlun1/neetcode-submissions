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
        incomplete = False

        while q:
            node = q.popleft()
            for nei in [node.left, node.right]:
                if incomplete and nei:
                    return False
                if nei:
                    q.append(nei)
                else:
                    incomplete = True

        return True
        
        