class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_total = sum(stones)
        target = stone_total // 2
        cache = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return abs(total - (stone_total - total))

            if (i, total) in cache:
                return cache[(i, total)]

            res = float("inf")
            for j in range(i, len(stones)):
                res = min(res, dfs(j + 1, total + stones[j]))

            cache[(i, total)] = res

            return res

        return dfs(0, 0)
        