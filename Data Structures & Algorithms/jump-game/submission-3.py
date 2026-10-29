class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]
            for jump in range(jumps, 0, -1):
                if i + jump >= len(nums):
                    continue

                dp[i] |= dp[i + jump]
                if dp[i]:
                    break

        return dp[0]
        