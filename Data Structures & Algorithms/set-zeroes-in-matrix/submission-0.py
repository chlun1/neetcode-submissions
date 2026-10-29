class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    for i in range(rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = None
                    for j in range(cols):
                        if matrix[r][j] != 0:
                            matrix[r][j] = None
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] is None:
                    matrix[r][c] = 0
        