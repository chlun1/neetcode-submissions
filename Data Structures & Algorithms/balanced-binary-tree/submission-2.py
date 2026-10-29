# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        curr = root
        stack = []
        last_visited = None
        heights = {}

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and last_visited != curr.right:
                curr = curr.right
            else:
                left_height = heights.get(curr.left, 0)
                right_height = heights.get(curr.right, 0)

                if abs(left_height - right_height) > 1:
                    return False
                
                heights[curr] = 1 + max(left_height, right_height)
                last_visited = stack.pop()
                curr = None

        return True

    def isBalanced_recursive(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        balanced = True
        
        def height(node):
            nonlocal balanced

            if not node:
                return 0
            if not balanced:
                return 0
            
            left_height = height(node.left)
            right_height = height(node.right)
            balanced &= (abs(left_height - right_height) <= 1)
            
            return 1 + max(left_height, right_height)

        height(root)
        return balanced
