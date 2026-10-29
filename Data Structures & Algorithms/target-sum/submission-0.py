class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}
    
        def dfs(i, total):
            if i >= len(nums):
                return 1 if total == target else 0
            if (i, total) in cache:
                return cache[(i, total)]

            res = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            cache[(i, total)] = res

            return res
    
        return dfs(0, 0)
            