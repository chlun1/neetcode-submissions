class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(i, -2, -1):
                res = dp[i + 1][j + 1]
                if j == -1 or nums[i] > nums[j]:
                    res = max(res, 1 + dp[i + 1][i + 1])

                dp[i][j + 1] = res

        return dp[0][0]
