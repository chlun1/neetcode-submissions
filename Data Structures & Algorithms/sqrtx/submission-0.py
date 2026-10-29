class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        res = -1

        while l <= r:
            mid = l + (r - l) // 2
            sq = mid * mid
            if sq == x:
                return mid
            if sq > x:
                r = mid - 1
            else:
                res = mid
                l = mid + 1

        return res
        