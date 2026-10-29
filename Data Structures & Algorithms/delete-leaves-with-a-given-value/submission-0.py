# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        curr = root
        stack = []
        last_visited = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and curr.right != last_visited:
                curr = curr.right
            else:
                if curr.left:
                    if (
                        curr.left.val == target
                        and not curr.left.left
                        and not curr.left.right
                    ):
                        curr.left = None
                if curr.right:
                    if (
                        curr.right.val == target
                        and not curr.right.left
                        and not curr.right.right
                    ):
                        curr.right = None
                last_visited = stack.pop()
                curr = None
        
        if root.val == target and not root.left and not root.right:
            return None

        return root