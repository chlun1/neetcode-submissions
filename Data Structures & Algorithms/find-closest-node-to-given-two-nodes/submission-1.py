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

        min_d = float("inf")
        res = -1

        for node in range(len(edges)):
            d1 = dist1.get(node, -1)
            d2 = dist2.get(node, -1)
            if d1 != -1 and d2 != -1:
                d = max(d1, d2)
                if d < min_d:
                    min_d = d
                    res = node

        return res
