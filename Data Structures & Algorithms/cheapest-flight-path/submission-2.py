import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        
        for u, v, price in flights:
            adj[u].append((v, price))

        min_heap = [(0, 0, src)]  # cost, stops, airport
        heapq.heapify(min_heap)
        visited = set()

        while min_heap:
            cost, stops, curr = heapq.heappop(min_heap)

            if curr == dst:
                return cost
            if (curr, stops) in visited or stops > k:
                continue

            visited.add((curr, stops))

            for nbr, price in adj[curr]:
                if (nbr, stops + 1) not in visited:
                    heapq.heappush(min_heap, (cost + price, stops + 1, nbr))

        return -1
    