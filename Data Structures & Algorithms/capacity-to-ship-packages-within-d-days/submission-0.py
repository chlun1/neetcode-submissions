import math


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def can_ship(capacity):
            t = 1
            ws = 0
            for w in weights:
                if ws + w > capacity:
                    t += 1
                    ws = 0
                    if t > days:
                        return False
                ws += w

            return True

        while l <= r:
            capacity = l + (r - l) // 2

            if can_ship(capacity):
                res = capacity
                r = capacity - 1
            else:
                l = capacity + 1

        return res
        