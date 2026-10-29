class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(amount + 1):
            for coin in coins:
                if a - coin >= 0 and dp[a - coin] != -1:
                    dp[a] = min(dp[a], 1 + dp[a - coin])
            
            if dp[a] == float("inf"):
                dp[a] = -1

        return dp[amount]
