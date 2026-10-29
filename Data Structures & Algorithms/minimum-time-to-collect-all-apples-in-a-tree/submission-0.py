from collections import deque


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        apples = [u for u in adj.keys() if hasApple[u]]
        predecessors = {}
        edges = set()

        for src in apples:
            q = deque([(src, 0)])
            visited = set([src])

            while q:
                u, dist = q.popleft()
                if u == 0:
                    while u != src:
                        parent = predecessors[u]
                        edges.add((parent, u))
                        u = parent
                    break

                for v in adj[u]:
                    if v not in visited:
                        q.append((v, dist + 1))
                        visited.add(v)
                        predecessors[v] = u

        return len(edges) * 2
