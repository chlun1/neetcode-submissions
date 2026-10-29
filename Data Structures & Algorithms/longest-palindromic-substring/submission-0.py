class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = True

        maxlen = 1
        res = s[0]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = (s[i] == s[j]) and dp[i + 1][j - 1]
            
                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    res = s[i: j + 1]

        return res
