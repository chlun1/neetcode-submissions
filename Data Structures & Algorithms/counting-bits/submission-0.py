import math


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n + 1):
            j = 2 ** math.floor(math.log(i, 2))
            res.append(res[i - j] + 1)

        return res
        