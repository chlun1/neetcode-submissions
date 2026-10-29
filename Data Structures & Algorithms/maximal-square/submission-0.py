from collections import deque


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        res = 0

        def bfs(i, j):
            q = deque([(i, j)])
            res = 0
            level = 1

            while q:
                if len(q) != 2 * level - 1:
                    return res

                res = level * level

                min_r = float("inf")
                min_c = float("inf")
                max_r = 0
                max_c = 0

                for _ in range(len(q)):
                    r, c = q.popleft()
                    min_r = min(min_r, r)
                    min_c = min(min_c, c)
                    max_r = max(max_r, r)
                    max_c = max(max_c, c)

                if max_c == cols - 1 or max_r == rows - 1:
                    return res

                for r in range(min_r, max_r + 1):
                    if matrix[r][max_c + 1] == "1":
                        q.append((r, max_c + 1))
                for c in range(min_c, max_c + 1):
                    if matrix[max_r + 1][c] == "1":
                        q.append((max_r + 1, c))

                if matrix[max_r + 1][max_c + 1] == "1":
                    q.append((max_r + 1, max_c + 1))

                level += 1

            return res

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    res = max(res, bfs(r, c))

        return res
        