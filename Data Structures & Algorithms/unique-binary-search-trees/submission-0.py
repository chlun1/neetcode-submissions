class Solution:
    def numTrees(self, n: int) -> int:
        res = 0
        cache = {}

        def dfs(k):
            if k == 0 or k == 1:
                return 1

            if k in cache:
                return cache[k]

            count = 0

            for i in range(1, k + 1):
                count += dfs(i - 1) * dfs(k - i)
            
            cache[k] = count
            return count

        return dfs(n)
