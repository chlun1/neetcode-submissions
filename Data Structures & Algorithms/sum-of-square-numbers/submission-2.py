class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)

        while l <= r:
            total = l ** 2 + r ** 2
            if total == c:
                return True
            if total < c:
                l += 1
            else:
                r -= 1

        return False
