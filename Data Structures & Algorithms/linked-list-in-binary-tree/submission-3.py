from collections import deque


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            node_ = stack.pop()

            if node_.val == head.val:
                q = deque([(node_, head)])

                while q:
                    for _ in range(len(q)):
                        node, curr = q.popleft()

                        curr = curr.next
                        if not curr:
                            return True

                        if node.left and node.left.val == curr.val:
                            q.append((node.left, curr))
                        if node.right and node.right.val == curr.val:
                            q.append((node.right, curr))
            
            if node_.left:
                stack.append(node_.left)
            if node_.right:
                stack.append(node_.right)
                    
        return False
