class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[-1] == "1":
            return False

        dp = [False] * len(s)
        dp[-1] = True

        for i in range(len(s) - 2, -1, -1):
            if s[i] == "1":
                continue

            for jump in range(maxJump, minJump - 1, -1):
                j = i + jump
                if j >= len(s):
                    continue

                dp[i] = dp[j]
                if dp[i]:
                    break

        return dp[0]
        