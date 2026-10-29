# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good = 0
        # node, max value seen so far on the path to node
        stack = [(root, root.val)]
        while stack:
            curr, curr_max = stack.pop()
            if curr.val >= curr_max:
                good += 1
            curr_max = max(curr_max, curr.val)
            if curr.left:
                stack.append((curr.left, curr_max))
            if curr.right:
                stack.append((curr.right, curr_max))

        return good
        