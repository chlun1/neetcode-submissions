class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        cache = {}

        def dfs(r, c, moves):
            if r < 0 or r == m or c < 0 or c == n:
                return 1

            if moves == maxMove:
                return 0

            key = (r, c, moves)

            if key in cache:
                return cache[key]

            res = 0

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                res += dfs(r + dr, c + dc, moves + 1)
                res %= 1000000007
                
            cache[key] = res
            return res

        return dfs(startRow, startColumn, 0)
