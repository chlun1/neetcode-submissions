class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        cache = [None] * len(s)

        def dfs(i):
            if i >= len(s) - 1:
                return True
            if cache[i] is not None:
                return cache[i]

            res = False

            for jump in range(maxJump, minJump - 1, -1):
                j = i + jump
                if j >= len(s) or s[j] == "1":
                    continue

                res |= dfs(j)
                if res:
                    break

            cache[i] = res

            return res

        return dfs(0)
        