from collections import defaultdict, deque


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        in_degrees = [0] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            in_degrees[u] += 1
            in_degrees[v] += 1

        q = deque([node for node in range(n) if in_degrees[node] == 1])

        while q:
            if n <= 2:
                return list(q)

            for _ in range(len(q)):
                node = q.popleft()
                n -= 1
    
                for nbr in adj[node]:
                    in_degrees[nbr] -= 1
                    if in_degrees[nbr] == 1:
                        q.append(nbr)
    