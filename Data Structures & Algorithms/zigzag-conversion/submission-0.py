import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        n = numRows + (numRows - 2)
        cols = math.ceil(2 * len(s) / n)
        grid = [[None] * cols for _ in range(numRows)]

        col = 0
        i = 0

        while i < len(s): 
            for row in range(numRows):
                grid[row][col] = s[i]
                i += 1

                if i == len(s):
                    break

            if i < len(s):
                col += 1
    
                for row in range(numRows - 2, 0, -1):
                    grid[row][col] = s[i]
                    i += 1

                    if i == len(s):
                        break
    
                col += 1

        res = []

        for row in range(numRows):
            for col in range(cols):
                if grid[row][col]:
                    res.append(grid[row][col])

        return "".join(res)


