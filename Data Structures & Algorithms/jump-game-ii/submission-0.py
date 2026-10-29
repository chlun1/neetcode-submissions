class Solution:
    def jump(self, nums: List[int]) -> int:
        cache = [None] * len(nums)
        
        def dfs(i):
            if i >= len(nums) - 1:
                return 0
    
            if cache[i] is not None:
                return cache[i]
    
            res = len(nums)
            for j in range(nums[i], 0, -1):
                res = min(res, 1 + dfs(i + j))
        
            cache[i] = res
    
            return res
    
        return dfs(0)
            