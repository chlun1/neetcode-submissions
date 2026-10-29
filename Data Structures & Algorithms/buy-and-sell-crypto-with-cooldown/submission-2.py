class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 2)]

        for i in range(len(prices) - 1, -1, -1):
            dp[i][True] = max(dp[i + 1][False] - prices[i], dp[i + 1][True])
            dp[i][False] = max(dp[i + 2][True] + prices[i], dp[i + 1][False])

        return dp[0][True]
        