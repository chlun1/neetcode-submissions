class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            if (
                r < 0 or r >= rows or c < 0 or c >= cols
                or grid[r][c] == 0
            ):
                return 1

            visited.add((r, c))

            perimeter = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = r + dr
                nc = c + dc

                if (nr, nc) not in visited:
                    perimeter += dfs(nr, nc)

            return perimeter

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return dfs(r, c)

        