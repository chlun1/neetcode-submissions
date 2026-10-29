# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path_sums = {None: 0}
        res = -float("inf")
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
                left_sum = max(0, path_sums[curr.left])
                right_sum = max(0, path_sums[curr.right])
                val = curr.val
                
                res = max(res, left_sum + val + right_sum)
                path_sums[curr] = val + max(left_sum, right_sum)

                last_visited = stack.pop()
                curr = None

        return res
        