class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cache = [None] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return False
            if i == len(nums) - 1:
                return True
            if cache[i] is not None:
                return cache[i]

            jumps = nums[i]
            res = False

            for jump in range(jumps, 0, -1):
                if dfs(i + jump):
                    res = True
                    break

            cache[i] = res

            return res

        return dfs(0)
        