# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, total):
            nonlocal res
            if not node:
                return

            new_total = 10 * total + node.val

            if not node.left and not node.right:
                res += new_total
                return

            if node.left:
                dfs(node.left, new_total)
            if node.right:
                dfs(node.right, new_total)
                
        dfs(root, 0)

        return res
