class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in cache:
                return cache[(i, j)]

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            # Next pattern is a *
            if j + 1 < len(p) and p[j + 1] == "*":
                res = dfs(i, j + 2)  # Skip to after *
                if match:
                    res |= dfs(i + 1, j)  # Use the *

                cache[(i, j)] = res
                return cache[(i, j)]

            # Current character is a match
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]

            cache[(i, j)] = False
            return cache[(i, j)]

        return dfs(0, 0)
