# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        money = {None: (0, 0)}  # Max amount if rob current, not rob current
        curr = root
        stack = []
        last_visited = None
        res = 0

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack[-1]
            if curr.right and curr.right != last_visited:
                curr = curr.right
            else:
                l1, l2 = money[curr.left]
                r1, r2 = money[curr.right]
                val = curr.val

                money[curr] = val + l2 + r2, max(l1, l2) + max(r1, r2)

                res = max(res, max(money[curr]))
                last_visited = stack.pop()
                curr = None

        return res
        