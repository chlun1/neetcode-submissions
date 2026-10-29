class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0
            if (i, can_buy) in cache:
                return cache[(i, can_buy)]

            # Do nothing
            res = dfs(i + 1, can_buy)

            if can_buy:
                # Buy
                res = max(res, dfs(i + 1, False) - prices[i])
            else:
                # Sell
                res = max(res, dfs(i + 2, True) + prices[i])

            cache[(i, can_buy)] = res
            return res

        return dfs(0, True)
        