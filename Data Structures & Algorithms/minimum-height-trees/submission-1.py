from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            if node in visited:
                return 0

            visited.add(node)
            height = 0

            for nbr in adj[node]:
                if nbr not in visited:
                    height = max(height, 1 + dfs(nbr))

            return height

        res = [[] for _ in range(n)]

        for node in range(n):
            visited = set()
            height = dfs(node)
            res[height].append(node)

        for nodes in res:
            if len(nodes) > 0:
                return nodes
        