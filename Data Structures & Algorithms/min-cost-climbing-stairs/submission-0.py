class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)

        def dfs(i):
            if i == n - 1:
                return cost[i]
            if i == n:
                return 0
            
            if i not in cache:
                cache[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))

            return cache[i]
        
        return min(dfs(0), dfs(1))
