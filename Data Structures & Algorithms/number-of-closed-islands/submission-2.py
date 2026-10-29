class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            stack = [(r, c)]
            res = True

            while stack:
                r, c = stack.pop()

                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    res = False

                grid[r][c] = 1

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr = r + dr
                    nc = c + dc
    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                        stack.append((nr, nc))

            return res

        res = 0

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if grid[r][c] == 0 and dfs(r, c):
                    res += 1

        return res
