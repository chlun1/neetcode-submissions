class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}

        def dfs(i, remaining):
            if i == len(days):
                return 0
            key = (i, remaining)
            if key in cache:
                return cache[key]

            if i > 0:
                prev = days[i - 1]
                day = days[i]
                gap = day - prev
    
                if remaining - gap >= 0:
                    cache[key] = dfs(i + 1, remaining - gap) 
                    return cache[key]

            res = float("inf")

            for passes, cost in zip([1, 7, 30], costs):
                res = min(res, cost + dfs(i + 1, passes - 1))

            cache[key] = res
            return res

        return dfs(0, 0)
