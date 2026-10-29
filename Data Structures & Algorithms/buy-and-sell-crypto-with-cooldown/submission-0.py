class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dfs(i, j):
            if i == len(prices) - 1:
                return prices[i] - prices[j] if j != -1 else 0
            if i >= len(prices):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]

            res = 0
            
            if j != -1:
                # Previously bought at jth day
                res = max(
                    res,
                    prices[i] - prices[j] + dfs(i + 2, -1),  # Sell
                    dfs(i + 1, j)  # Hold
                )
            else:
                res = max(
                    dfs(i + 1, j),  # Don't buy
                    dfs(i + 1, i),  # Buy
                )

            cache[(i, j)] = res

            return res

        return dfs(0, -1)
        