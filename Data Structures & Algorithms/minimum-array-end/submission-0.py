class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        ni = 1
        xi = 1
        res = x

        while ni <= n:
            if x & xi == 0:
                if n & ni != 0:
                    res |= xi
                ni <<= 1
            xi <<= 1

        return res
