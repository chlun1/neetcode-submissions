# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        res = []
        def preorder(node):
            if not node:
                res.append("null")
                return
            
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        preorder(root)

        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        nodes = data.split(",")

        idx = 0
        def build():
            nonlocal idx

            if idx == len(nodes):
                return None
        
            val = nodes[idx]
            if val == "null":
                idx += 1
                return None

            node = TreeNode(val)
            idx += 1
            node.left = build()
            node.right = build()

            return node

        return build()
