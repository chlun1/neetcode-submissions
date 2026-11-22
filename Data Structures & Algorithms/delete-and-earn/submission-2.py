from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        vals = defaultdict(int)
        for num in nums:
            vals[num] += num

        nums = list(sorted(vals.keys()))
        cache = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in cache:
                return cache[i]

            j = i + 2 if i < len(nums) - 1 and nums[i + 1] == nums[i] + 1 else i + 1
            res = max(dfs(i + 1), dfs(j) + vals[nums[i]])

            cache[i] = res

            return res

        return dfs(0)
