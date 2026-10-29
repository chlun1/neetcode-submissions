class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][a] represents the number of ways to form amount a
        # using coins from index i onward.
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][0] = 1
        
        for i in range(len(coins) -1, -1, -1):
            for a in range(amount + 1):
                dp[i][a] = dp[i + 1][a]
                if a >= coins[i]:
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]
        