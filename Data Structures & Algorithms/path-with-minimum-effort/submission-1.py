import heapq


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        min_heap = [(0, (0, 0))]
        heapq.heapify(min_heap)
        efforts = {}

        while min_heap:
            effort, (r, c) = heapq.heappop(min_heap)

            if (r, c) in efforts:
                continue

            efforts[(r, c)] = effort

            if (r, c) == (rows - 1, cols - 1):
                break

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and 0 <= nc < cols
                    and (nr, nc) not in efforts
                ):
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    heapq.heappush(min_heap, (new_effort, (nr, nc)))

        return efforts[(rows - 1, cols - 1)]
        