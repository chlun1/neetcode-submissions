class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        res = []
        increment = 2 * (numRows - 1)

        for row in range(numRows):
            for i in range(row, len(s), increment):
                res.append(s[i])
                if (
                    0 < row < numRows - 1
                    and i + increment - 2 * row < len(s)
                ):
                    res.append(s[i + increment - 2 * row])

        return "".join(res)
