import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {i: [] for i in range(n)}
        
        for u, v, price in flights:
            adj[u].append((v, price))

        min_heap = [(0, 0, src)]  # cost, stops, airport
        heapq.heapify(min_heap)
        visited = set()

        print(adj)

        while min_heap:
            print(min_heap)
            cost, stops, curr = heapq.heappop(min_heap)

            if curr == dst:
                return cost
            if stops > k:
                print(f"stops {stops} > {k}")
                continue

            visited.add(curr)

            for nbr, price in adj[curr]:
                if nbr not in visited:
                    print(f"pushed ({cost + price}, {stops + 1}, {nbr}) to heap")
                    heapq.heappush(min_heap, (cost + price, stops + 1, nbr))

        return -1
