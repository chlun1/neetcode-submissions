import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, t in times:
            adj[u].append((t, v))

        min_heap = [(0, k)]
        heapq.heapify(min_heap)
        visited = set()

        while min_heap:
            t, u = heapq.heappop(min_heap)

            if u in visited:
                continue

            visited.add(u)

            if len(visited) == n:
                return t

            for dt, v in adj[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (t + dt, v))

        return -1
