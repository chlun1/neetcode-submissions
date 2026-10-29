class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[rows - 1][cols - 1] = grid[rows - 1][cols - 1]

        for r in range(rows - 2, -1, -1):
            dp[r][cols - 1] = grid[r][cols - 1] + dp[r + 1][cols - 1]
        for c in range(cols - 2, -1, -1):
            dp[rows - 1][c] = grid[rows - 1][c] + dp[rows - 1][c + 1]

        for r in range(rows - 2, -1, -1):
            for c in range(cols - 2, -1, -1):
                dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]
        