class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        cache = {}

        def dfs(i):
            if i == len(s) - 1:
                return 0 if s[i] == "0" else 1
            if i > len(s) - 1:
                return 1
            if s[i] == "0":
                return 0

            if i in cache:
                return cache[i]

            res = dfs(i + 1)
            if int(s[i] + s[i + 1]) <= 26:
                res += dfs(i + 2)

            cache[i] = res
            return res

        return dfs(0)
