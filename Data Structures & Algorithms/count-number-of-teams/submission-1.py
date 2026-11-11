class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def dfs(i, curr, increasing):
            if len(curr) == 3:
                return 1

            key = (i, len(curr), curr[-1]) if curr else i
            cached = cache.get(key)
            if cached:
                return cached

            res = 0
    
            for j in range(i, len(rating)):
                r = rating[j]
                if (
                    not curr
                    or (increasing and r > curr[-1])
                    or (not increasing and r < curr[-1])
                ):
                    curr.append(r)
                    res += dfs(j + 1, curr, increasing)
                    curr.pop()

            cache[key] = res
            return res

        res = 0
        cache = {}
        res += dfs(0, [], True)
        cache = {}
        res += dfs(0, [], False)

        return res
