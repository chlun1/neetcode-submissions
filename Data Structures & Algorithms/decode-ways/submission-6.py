class Solution:
    def numDecodings(self, s: str) -> int:
        dp1 = 0 if s[-1] == "0" else 1
        dp2 = 1
        
        for i in range(len(s) - 2, -1, -1):
            tmp = 0
            if s[i] != "0":
                tmp += dp1
                if int(s[i] + s[i + 1]) <= 26:
                    tmp += dp2

            dp1, dp2 = tmp, dp1

        return dp1
