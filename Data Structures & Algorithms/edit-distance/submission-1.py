class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 - 1, -1, -1):
            dp[i][n2] = 1 + dp[i + 1][n2]
        for j in range(n2 - 1, -1, -1):
            dp[n1][j] = 1 + dp[n1][j + 1]

        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i + 1][j + 1],
                        dp[i][j + 1],
                        dp[i + 1][j],
                    )

        return dp[0][0]
        