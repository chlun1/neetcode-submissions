class Solution:
    def coloredCells(self, n: int) -> int:
        # 1 + \sum_{i=1}^{n-1} 4i = 1 + 4 n (n - 1) / 2
        return 1 + 2 * n * (n - 1)
