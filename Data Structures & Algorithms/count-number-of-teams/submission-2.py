class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def dfs(i, count, increasing):
            if count == 3:
                return 1

            key = (i, count)
            cached = cache.get(key)
            if cached:
                return cached

            res = 0
            prev_rating = rating[i]
    
            for j in range(i + 1, len(rating)):
                r = rating[j]
                if (
                    count == 0
                    or (increasing and r > prev_rating)
                    or (not increasing and r < prev_rating)
                ):
                    res += dfs(j, count + 1, increasing)

            cache[key] = res
            return res

        res = 0
        cache = {}
        res += dfs(-1, 0, True)
        cache = {}
        res += dfs(-1, 0, False)

        return res
