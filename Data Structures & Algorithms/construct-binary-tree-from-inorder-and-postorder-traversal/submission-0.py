# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        n = len(postorder)
        root = TreeNode(postorder[-1])
        i = inorder.index(root.val)

        root.left = self.buildTree(
            inorder[:i],
            postorder[:i],
        )
        root.right = self.buildTree(
            inorder[i + 1:],
            postorder[i: n - 1],
        )

        return root
