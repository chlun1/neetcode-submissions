from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        nums = list(sorted(counts.keys()))
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            j = i + 2 if i < n - 1 and nums[i + 1] == nums[i] + 1 else i + 1
            dp[i] = max(dp[i + 1], dp[j] + nums[i] * counts[nums[i]])

        return dp[0]
