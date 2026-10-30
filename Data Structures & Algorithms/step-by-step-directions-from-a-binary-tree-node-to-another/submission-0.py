from collections import defaultdict, deque


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj = defaultdict(list)
        stack = [root]

        while stack:
            curr = stack.pop()
            
            if curr.left:
                adj[curr.val].append((curr.left, "L"))
                adj[curr.left.val].append((curr, "U"))
                stack.append(curr.left)
            if curr.right:
                adj[curr.val].append((curr.right, "R"))
                adj[curr.right.val].append((curr, "U"))
                stack.append(curr.right)

        predecessors = {}
        q = deque([startValue])
        visited = set([startValue])

        while q:
            curr = q.popleft()

            if curr == destValue:
                break

            for nei, d in adj[curr]:
                if nei.val not in visited:
                    q.append(nei.val)
                    predecessors[nei.val] = (curr, d)
                    visited.add(nei.val)

        curr = destValue
        res = []

        while curr != startValue:
            curr, d = predecessors[curr]
            res.append(d)

        return "".join(res[::-1])
