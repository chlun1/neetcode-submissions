class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}

        def dfs(curr_sum):
            if curr_sum > target:
                return 0
            if curr_sum == target:
                return 1
            if curr_sum in cache:
                return cache[curr_sum]

            res = 0

            for j in range(len(nums)):
                curr_sum += nums[j]
                res += dfs(curr_sum)
                curr_sum -= nums[j]

            cache[curr_sum] = res

            return res

        return dfs(0)
