import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [[float("inf")] * (k + 5) for _ in range(n)]
        adj = defaultdict(list)

        for u, v, p in flights:
            adj[u].append((v, p))

        min_heap = [(0, 0, src)]

        while min_heap:
            cost, stops, u = heapq.heappop(min_heap)

            if u == dst:
                return cost
            if cost > costs[u][stops] or stops > k:
                continue

            for v, price in adj[u]:
                new_cost = cost + price
                if new_cost < costs[v][stops + 1]:
                    costs[v][stops + 1] = new_cost
                    heapq.heappush(min_heap, (new_cost, stops + 1, v))

        return -1
        