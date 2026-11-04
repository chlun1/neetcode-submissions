class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        res = [[1], [1,1]]

        for i in range(numRows - 2):
            row = [1] * (i + 3)
            prev_row = res[-1]

            for j in range(1, i + 2):
                row[j] = prev_row[j - 1] + prev_row[j]

            res.append(row)

        return res
        