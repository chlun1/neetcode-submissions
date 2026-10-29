class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        cache = {}

        def dfs(j, arr):
            if j == len(nums):
                return 0

            key = (j, tuple(arr))
            if key in cache:
                return cache[key]

            res = 0

            for i in range(len(arr)):
                prod = (
                    (arr[i - 1] if i - 1 >= 0 else 1)
                    * arr[i]
                    * (arr[i + 1] if i + 1 < len(arr) else 1)
                )
                res = max(res, prod + dfs(j + 1, arr[:i] + arr[i + 1:]))

            cache[key] = res
            return res

        return dfs(0, nums)
        