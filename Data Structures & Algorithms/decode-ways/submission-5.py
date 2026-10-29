class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[-1] = 1
        dp[-2] = 1 if s[-1] != "0" else 0

        for i in range(n - 2, -1, -1):
            if s[i] != "0":
                dp[i] = dp[i + 1]
                if int(s[i] + s[i + 1]) <= 26:
                    dp[i] += dp[i + 2]

        return dp[0]
        