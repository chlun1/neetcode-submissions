class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i, j):
            """i: curr index, j: index of previously chosen number"""
            if i == len(nums):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            res = 0
            if j == -1 or nums[j] < nums[i]:
                res = dfs(i + 1, i) + 1
            
            res = max(res, dfs(i + 1, j))
            cache[(i, j)] = res

            return res

        return dfs(0, -1)
