class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dfs(i, total):
            if i >= len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            if (i, total) in cache:
                return cache[(i, total)]

            res = 0
            for j in range(i, len(coins)):
                res += dfs(j, total + coins[j])

            cache[(i, total)] = res

            return res

        return dfs(0, 0)
        