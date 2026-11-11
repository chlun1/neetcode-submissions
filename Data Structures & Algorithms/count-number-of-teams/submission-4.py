class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0

        for m in range(1, len(rating) - 1):
            mid = rating[m]
            l_small, r_large = 0, 0
            l_large, r_small = 0, 0

            for i in range(m):
                if rating[i] < mid:
                    l_small += 1
                elif rating[i] > mid:
                    l_large += 1

            for i in range(m + 1, len(rating)):
                if rating[i] > mid:
                    r_large += 1
                elif rating[i] < mid:
                    r_small += 1

            res += l_small * r_large + l_large * r_small

        return res
