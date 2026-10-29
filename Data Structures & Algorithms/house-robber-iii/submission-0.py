# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Return max that can be robbed by robbing the current node
        # and without robbing the current node.
        def dfs(node):
            if not node:
                return 0, 0
            
            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)

            return node.val + l2 + r2, max(l1, l2) + max(r1, r2)

        return max(dfs(root))
