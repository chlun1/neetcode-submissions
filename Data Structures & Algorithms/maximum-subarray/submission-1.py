class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cache = {}
        max_sum = -float("inf")

        def dfs(i, curr):
            nonlocal max_sum
            max_sum = max(max_sum, curr)

            if i == len(nums):
                return curr
            if (i, curr) in cache:
                return cache[(i, curr)]

            # Continue the subarray
            res = dfs(i + 1, curr + nums[i])
            # Start fresh
            res = max(res, dfs(i + 1, nums[i]))

            cache[(i, curr)] = res

            return res

        dfs(1, nums[0])
        return max_sum
        