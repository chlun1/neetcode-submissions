from collections import defaultdict, deque


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        routes = [set(r) for r in routes]
        stop_to_route = defaultdict(list)
        for route_idx, stops in enumerate(routes):
            for stop in stops:
                stop_to_route[stop].append(route_idx)

        graph = defaultdict(list)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                if routes[i].intersection(routes[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        if source not in stop_to_route or target not in stop_to_route:
            return -1

        q = deque(stop_to_route[source])
        visited = set(stop_to_route[source])
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                route_idx = q.popleft()

                if target in routes[route_idx]:
                    return res

                for next_route_idx in graph[route_idx]:
                    if next_route_idx not in visited:
                        q.append(next_route_idx)
                        visited.add(next_route_idx)

        return -1
