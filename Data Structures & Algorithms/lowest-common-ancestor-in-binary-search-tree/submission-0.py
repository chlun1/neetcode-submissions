# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        res = None

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left_res = dfs(node.left)
            right_res = dfs(node.right)

            if left_res + right_res == 2:
                if not res:
                    res = node
                return 2
            
            if node.val in (p.val, q.val):
                total = 1 + left_res + right_res
                if total == 2:
                    if not res:
                        res = node
                return total

            return left_res + right_res

        dfs(root)

        return res
            