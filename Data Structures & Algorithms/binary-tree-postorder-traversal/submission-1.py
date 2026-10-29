# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal_old(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return res[::-1]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = []
        current = root
        last_visited = None
        curr = root

        """
        while current or stack:
            if current:
                stack.append(current)
                current = current.left
                
            # Step 2: When you can't go left anymore, peek at the top node
            else:
                peek_node = stack[-1]
                
                # Step 3: If it has a right child AND we haven't just returned from it
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right # Traverse down the right side
                    
                # Step 4: Otherwise, both left and right are done. Process the node!
                else:
                    res.append(peek_node.val)
                    last_visited = stack.pop()

        return res
        """

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack[-1]
            if curr.right and last_visited != curr.right:
                curr = curr.right
            else:
                res.append(curr.val)
                last_visited = stack.pop()
                curr = None
            
        return res
