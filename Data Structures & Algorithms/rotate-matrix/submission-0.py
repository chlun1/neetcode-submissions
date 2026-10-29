class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows // 2):
            matrix[row], matrix[rows - row - 1] = (
                matrix[rows - row - 1], matrix[row]
            )

        for i in range(rows):
            for j in range(i + 1, cols):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
