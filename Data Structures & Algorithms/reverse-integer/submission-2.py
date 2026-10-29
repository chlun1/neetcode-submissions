class Solution:
    def reverse(self, x: int) -> int:
        max_int = 2 ** 31 - 1
        is_negative = x < 0
        x = abs(x)
        res = 0

        while x != 0:
            digit = x % 10
            if res > max_int // 10 or (res == max_int // 10 and digit > max_int % 10):
                return 0
            res = (res * 10) + digit
            x //= 10

        return -res if is_negative else res
        