class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        dup = None
        total = 0

        for r in range(n):
            for c in range(n):
                num = grid[r][c]
                total += num
                if dup is None:
                    if num in seen:
                        dup = num
                    seen.add(num)

        n2 = n ** 2
        expected = n2 * (n2 + 1) // 2

        return [dup, expected - total + dup]
        