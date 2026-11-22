from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        nums = list(sorted(counts.keys()))
        cache = {}

        def dfs(i, curr):
            if i >= len(nums):
                return curr

            key = (i, curr)
            if key in cache:
                return cache[key]

            res = dfs(i + 1, curr)
            j = i + 2 if i < len(nums) - 1 and nums[i + 1] == nums[i] + 1 else i + 1
            res = max(res, dfs(j, curr + nums[i] * counts[nums[i]]))

            cache[key] = res

            return res

        return dfs(0, 0)
