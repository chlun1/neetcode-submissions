class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        cols = set()
        diag = set()
        off_diag = set()
        
        def backtrack(r, curr):
            if r == n:
                res.append(["".join(x) for x in curr])
                return

            for c in range(n):
                if (
                    c in cols or
                    r - c in diag or
                    r + c in off_diag
                ):
                    continue

                curr[r][c] = "Q"
                cols.add(c)
                diag.add(r - c)
                off_diag.add(r + c)
                backtrack(r + 1, curr)
                curr[r][c] = "."
                cols.remove(c)
                diag.remove(r - c)
                off_diag.remove(r + c)

        backtrack(0, [["."] * n for _ in range(n)])

        return res
