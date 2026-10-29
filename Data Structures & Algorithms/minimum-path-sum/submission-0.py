class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        cache = {}

        def dfs(r, c):
            if r >= rows or c >= cols:
                return float("inf")
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if (r, c) in cache:
                return cache[(r, c)]
            
            res = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            cache[(r, c)] = res

            return res

        return dfs(0, 0)
        