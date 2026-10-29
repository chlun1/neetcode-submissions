class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n % 2 == 0:
                return helper(x * x, n // 2)
            else:
                return x * helper(x * x, (n - 1) // 2)

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
        