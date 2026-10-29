class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        min_heights = [[heights[0], 0]]
        res = heights[0]

        for i in range(1, len(heights)):
            if heights[i] <= min_heights[-1][0]:
                while min_heights and heights[i] <= min_heights[-1][0]:
                    _, j = min_heights.pop()
                min_heights.append([heights[i], j])
            else:
                min_heights.append([heights[i], i])

            for h, j in min_heights:
                res = max(res, h * (i - j + 1))

        return res
