class Solution:
    def _rob(self, nums: List[int]) -> int:
        cache = {}

        def dfs(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in cache:
                cache[i] = max(dfs(i - 1), dfs(i - 2) + nums[i])

            return cache[i]
            
        return dfs(len(nums) - 1)

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums[:-1]), self._rob(nums[1:]))
