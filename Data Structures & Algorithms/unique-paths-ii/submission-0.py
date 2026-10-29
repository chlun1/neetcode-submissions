class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        cache = {}

        def dfs(r, c):
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]

            res = 0
            if r < rows - 1:
                res += dfs(r + 1, c)
            if c < cols - 1:
                res += dfs(r, c + 1)

            cache[(r, c)] = res
            return res

        return dfs(0, 0)
        