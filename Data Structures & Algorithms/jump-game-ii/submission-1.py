class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[-1] = 0

        for i in range(len(nums) - 1, -1, -1):
            for jump in range(nums[i], 0, -1):
                if i + jump >= len(nums):
                    continue
                
                dp[i] = min(dp[i], 1 + dp[i + jump])

        return dp[0]
        