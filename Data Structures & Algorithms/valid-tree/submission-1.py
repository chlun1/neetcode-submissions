from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = set()
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for nbr in adj[node]:
                if nbr == prev:
                    continue
                if not dfs(nbr, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
