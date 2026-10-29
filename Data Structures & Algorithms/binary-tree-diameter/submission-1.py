# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        curr = root
        stack = []
        last_visited = None
        mp = {None: (0, 0)}

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and curr.right != last_visited:
                curr = curr.right
            else:
                left_height, left_dia = mp[curr.left]
                right_height, right_dia = mp[curr.right]

                mp[curr] = (
                    1 + max(left_height, right_height),
                    max(left_height + right_height, left_dia, right_dia)
                )

                last_visited = stack.pop()
                curr = None
        
        return mp[root][1]
