class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [height[0]] * n
        right = [height[-1]] * n
        res = 0

        for i in range(1, n):
            left[i] = max(height[i], left[i - 1])

        for i in range(n - 2, -1, -1):
            right[i] = max(height[i], right[i + 1])

        for i in range(n):
            res += min(left[i], right[i]) - height[i]

        return res

        