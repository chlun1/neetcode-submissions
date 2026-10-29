class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1

        for _ in range(abs(n)):
            res *= x

        return res if n >= 0 else 1 / res
        