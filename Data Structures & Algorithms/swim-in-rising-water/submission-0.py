import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        heapq.heapify(min_heap)
        visited = set()

        while min_heap:
            elev, r, c = heapq.heappop(min_heap)

            if (r, c) in visited:
                continue
            if (r, c) == (n - 1, n - 1):
                return elev
            
            visited.add((r, c))

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < n and 0 <= nc < n
                    and (nr, nc) not in visited
                ):
                    new_elev = max(elev, grid[nr][nc])
                    heapq.heappush(min_heap, (new_elev, nr, nc))
            