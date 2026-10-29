import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        l = math.ceil(total / h)
        r = max(piles)

        while l <= r:
            k = l + (r - l) // 2
            t = sum(math.ceil(p / k) for p in piles)
            if t <= h:
                r = k - 1
            else:
                l = k + 1

        return l
