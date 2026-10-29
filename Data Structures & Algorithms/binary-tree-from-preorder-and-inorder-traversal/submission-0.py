# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                root.left = self.buildTree(
                    preorder[1: i + 1],
                    inorder[:i],
                )
                root.right = self.buildTree(
                    preorder[i + 1:],
                    inorder[i + 1:],
                )
                break

        return root
