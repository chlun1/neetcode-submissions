class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, j):
            if i >= len(nums):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            res = dfs(i + 1, j)
            if j == -1 or nums[j] < nums[i]:
                res = max(res, 1 + dfs(i + 1, i))

            cache[(i, j)] = res

            return res

        return dfs(0, -1)
        