# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False

            stack = [(p, q)]
            while stack:
                u, v = stack.pop()
                if (u and not v) or (not u and v):
                    return False
                if u and v:
                    if u.val != v.val:
                        return False
                    stack.append((u.left, v.left))
                    stack.append((u.right, v.right))
            
            return True

        if not root and not subRoot:
            return True
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.val == subRoot.val:
                if is_same(curr, subRoot):
                    return True
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        
        return False
        