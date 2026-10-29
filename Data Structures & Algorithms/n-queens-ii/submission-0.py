class Solution:
    def totalNQueens(self, n: int) -> int:
        res = 0
        col = set()
        diag = set()
        off_diag = set()

        def backtrack(r):
            nonlocal res
            if r == n:
                res += 1
                return

            for c in range(n):
                if (
                    c in col
                    or r - c in diag
                    or r + c in off_diag
                ):
                    continue

                col.add(c)
                diag.add(r - c)
                off_diag.add(r + c)
                backtrack(r + 1)
                col.remove(c)
                diag.remove(r - c)
                off_diag.remove(r + c)

        backtrack(0)
        return res
