class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        
        def helper(l, r, t, b):
            nonlocal res
            res += [matrix[t][x] for x in range(l, r + 1)]
            res += [matrix[x][r] for x in range(t + 1, b + 1)]
            if t < b:
                res += [matrix[b][x] for x in range(r - 1, l - 1, -1)]
            if l < r:
                res += [matrix[x][l] for x in range(b - 1, t, -1)]

        l, r, t, b = 0, cols - 1, 0, rows - 1

        while l <= r and t <= b:
            helper(l, r, t, b)
            l += 1
            r -= 1
            t += 1
            b -= 1

        return res
