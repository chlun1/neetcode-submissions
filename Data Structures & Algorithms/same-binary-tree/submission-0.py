# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False

        stack = [(p, q)]

        while stack:
            u, v  = stack.pop()
            if (u and not v) or (not u and v):
                return False
            if u and v:
                if u.val != v.val:
                    return False
                stack.append((u.left, v.left))
                stack.append((u.right, v.right))

        return True
