from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        variables = set()
        for (a, b), val in zip(equations, values):
            adj[a].append((b, val))
            adj[b].append((a, 1 / val))
            variables.add(a)
            variables.add(b)

        def dfs(node, target):
            if node == target:
                return 1

            if node in visited:
                return -1
            
            visited.add(node)

            for nbr, val in adj[node]:
                if nbr not in visited:
                    prod = dfs(nbr, target)
                    if prod != -1:
                        return prod * val

            return -1

        res = []
        for q1, q2 in queries:
            if q1 not in variables or q2 not in variables:
                res.append(-1.0)
            else:
                visited = set()
                res.append(dfs(q1, q2))

        return res
