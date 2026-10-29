from collections import defaultdict, deque


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        adj = defaultdict(list)
        in_degrees = [0] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            in_degrees[u] += 1
            in_degrees[v] += 1

        q = deque([i for i in range(n) if in_degrees[i] == 1])

        while q:
            u = q.popleft()
            in_degrees[u] -= 1
            for v in adj[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 1:
                    q.append(v)

        for u, v in reversed(edges):
            if in_degrees[u] > 0 and in_degrees[v] > 0:
                return [u, v]
