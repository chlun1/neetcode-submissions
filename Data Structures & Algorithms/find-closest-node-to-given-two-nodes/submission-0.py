from collections import deque


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def bfs(src):
            q = deque([src])
            visited = set([src])

            dist = {}
            d = 0

            while q:
                node = q.popleft()
                dist[node] = d
                
                if edges[node] != -1:
                    nei = edges[node]
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)

                d += 1

            return dist

        dist1 = bfs(node1)
        dist2 = bfs(node2)

        dist = [-1] * len(edges)

        for node, d in dist1.items():
            if node in dist2:
                dist[node] = max(d, dist2[node])

        min_d = float("inf")
        res = -1

        for node, d in enumerate(dist):
            if d != -1:
                if d < min_d:
                    min_d = d
                    res = node

        return res
