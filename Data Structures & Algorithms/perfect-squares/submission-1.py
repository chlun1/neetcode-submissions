class Solution:
    def numSquares(self, n: int) -> int:
        r = int(n ** 0.5)

        dp = [n] * (n + 1)
        dp[0] = 0

        for t in range(1, n + 1):
            for i in range(1, r + 1):
                num = i ** 2
                if t - num >= 0:
                    dp[t] = min(dp[t], 1 + dp[t - num])

        return dp[n]
        