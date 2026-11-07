class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        r = n % 7
        res = 0

        for i in range(weeks):
            res += ((7 + i) * (7 + i + 1) // 2) - (i * (i + 1) // 2)

        res += ((r + weeks) * (r + weeks + 1) // 2) - (weeks * (weeks + 1) // 2)

        return res
