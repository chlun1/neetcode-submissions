class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            b1 = a & (1 << i)
            b2 = b & (1 << i)
            res |= b1 ^ b2 ^ carry
            carry = ((b1 & b2) | (b1 & carry) | (b2 & carry)) << 1

        if res > 2147483647:
            res = ~(res ^ 4294967295)

        return res
