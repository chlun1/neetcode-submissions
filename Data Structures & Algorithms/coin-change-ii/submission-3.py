class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i][a] = number of ways to form "amount" using coins
        # from ith index onwards and starting from subtotal a
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            dp[i][amount] = 1
        
        for i in range(len(coins) -1, -1, -1):
            for a in range(amount, -1, -1):
                dp[i][a] = dp[i + 1][a]
                if a + coins[i] <= amount:
                    dp[i][a] += dp[i][a + coins[i]]

        return dp[0][0]
        