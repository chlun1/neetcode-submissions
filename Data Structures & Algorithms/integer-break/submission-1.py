class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n, -1, -1):
            for num in range(1, n):
                if i - num >= 0:
                    dp[i - num] = max(dp[i - num], num * dp[i])

        return dp[0]
        