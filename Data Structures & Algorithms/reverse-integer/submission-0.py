import math


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0

        max_int = 2 ** 31 -1
        is_negative = x < 0
        x = abs(x)
        power = math.floor(math.log10(x))
        res = 0

        while x != 0:
            digit = x % 10
            if res + (digit * 10 ** power) > max_int:
                return 0
            res += digit * 10 ** power
            x //= 10
            power -= 1

        return -res if is_negative else res
        