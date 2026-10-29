# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        
        curr = root
        stack = []
        found = defaultdict(int)
        last_visited = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and curr.right != last_visited:
                curr = curr.right
            else:
                found_left = found[curr.left]
                found_right = found[curr.right]

                if found_left + found_right == 2:
                    return curr

                found[curr] = found_left + found_right
                if curr.val in (p.val, q.val):
                    found[curr] += 1
                if found[curr] == 2:
                    return curr
                last_visited = stack.pop()
                curr = None

        return root

    def lowestCommonAncestor_recursive(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        res = None

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left_res = dfs(node.left)
            right_res = dfs(node.right)

            if left_res + right_res == 2:
                if not res:
                    res = node
                return 2
            
            if node.val in (p.val, q.val):
                total = 1 + left_res + right_res
                if total == 2:
                    if not res:
                        res = node
                return total

            return left_res + right_res

        dfs(root)

        return res
            