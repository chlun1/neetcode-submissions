class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber > 0:
            offset = (columnNumber - 1) % 26
            res.append(chr(ord("A") + offset))
            columnNumber = (columnNumber - 1) // 26

        return "".join(res[::-1])
