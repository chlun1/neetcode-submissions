class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for M in range(1, n + 1):
                dp[i][M][0] = float("inf")
                dp[i][M][1] = 0
                stones = 0

                for j in range(i, min(i + (2 * M), n)):
                    stones += piles[j]

                    dp[i][M][0] = min(
                        dp[i][M][0],
                        dp[j + 1][max(M, j - i + 1)][1]
                    )
                    dp[i][M][1] = max(
                        dp[i][M][1],
                        dp[j + 1][max(M, j - i + 1)][0] + stones
                    )

        return dp[0][1][1]
