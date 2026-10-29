class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(1 << 5):
            if (n & (1 << i)) != 0:
                res |= (1 << (31 - i))

        return res
        