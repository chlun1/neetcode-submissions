class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n ** 2
        grid_sum = 0
        grid_sq_sum = 0

        for r in range(n):
            for c in range(n):
                grid_sum += grid[r][c]
                grid_sq_sum += grid[r][c] ** 2

        expected_sum = n2 * (n2 + 1) // 2
        expected_sq_sum = n2 * (n2 + 1) * (2 * n2 + 1) // 6
        diff = grid_sum - expected_sum  # a - b
        sq_diff = grid_sq_sum - expected_sq_sum  # a^2 - b^2
        ab = sq_diff // diff  # a + b

        a = (ab + diff) // 2  # a = (a + b) + (a - b)
        b = ab - a  # a = (a + b) - a

        return [a, b]
