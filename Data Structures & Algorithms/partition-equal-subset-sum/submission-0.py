class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        cache = {}

        def dfs(i, subset_sum):
            if subset_sum > total // 2:
                return False

            if subset_sum == total // 2:
                return True 

            key = (i, subset_sum)
            if key in cache:
                return cache[key]

            for j in range(i, len(nums)):
                subset_sum += nums[j]
                if dfs(j + 1, subset_sum):
                    cache[key] = True
                    return True
                subset_sum -= nums[j]

            cache[key] = False
            return False

        return dfs(0, 0)
        