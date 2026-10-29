from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        num_fresh = 0
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    num_fresh += 1

        if num_fresh == 0:
            return 0

        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + dr
                    nc = c + dc
                    if (
                        0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        num_fresh -= 1

            time += 1

        return time if num_fresh == 0 else -1
        