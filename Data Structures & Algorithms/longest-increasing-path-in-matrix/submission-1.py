class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]

            res = 1

            """
            Looping [(0, 1), (0, -1), (1, 0), (-1, 0)] leads to
            "RecursionError: maximum recursion depth exceeded"
            due to test cases that "snakes":

            (Start)
                1  ->  2  ->  3  ->  4
                                     |
                8  <-  7  <-  6  <-  5
                |
                9  -> 10  -> 11  -> 12
            """
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and matrix[r][c] < matrix[nr][nc]
                ):
                    res = max(res, 1 + dfs(nr, nc))

            cache[(r, c)] = res

            return res
        
        ans = 0
        for r in range(rows):
            for c in range(cols):
                ans = max(ans, dfs(r, c))
        
        return ans
