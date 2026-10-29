# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 0)]
        res = 0

        while stack:
            node, total = stack.pop()

            new_total = 10 * total + node.val
            if not node.left and not node.right:
                res += new_total
            else:
                if node.left:
                    stack.append((node.left, new_total))
                if node.right:
                    stack.append((node.right, new_total))
            
        return res
