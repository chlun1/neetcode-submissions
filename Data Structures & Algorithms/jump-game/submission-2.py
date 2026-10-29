class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            for jump in range(1, jumps + 1):
                if i + jump >= len(nums):
                    break

                dp[i] |= dp[i + jump]

        return dp[0]
        