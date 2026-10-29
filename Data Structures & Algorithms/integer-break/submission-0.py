class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dfs(curr_sum):
            if curr_sum == n:
                return 1
            if curr_sum in cache:
                return cache[curr_sum]

            res = 1

            for num in range(1, n):
                if curr_sum + num > n:
                    break
                res = max(res, num * dfs(curr_sum + num))

            cache[curr_sum] = res

            return res

        return dfs(0)
        