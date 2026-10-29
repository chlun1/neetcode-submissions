# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        
        # (node, min_thresh, max_thresh)
        stack = [(root, -float("inf"), float("inf"))]
        while stack:
            curr, min_thresh, max_thresh = stack.pop()
            if not (min_thresh < curr.val < max_thresh):
                return False
            if curr.left:
                stack.append((curr.left, min_thresh, curr.val))
            if curr.right:
                stack.append((curr.right, curr.val, max_thresh))

        return True
