from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        l = 0
        res = 0

        for r in range(len(fruits)):
            counts[fruits[r]] += 1
            
            while len(counts) > 2:
                f = fruits[l]
                counts[f] -= 1
                if counts[f] == 0:
                    del counts[f]
                l += 1

            res = max(res, r - l + 1)

        return res
        