class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            stack.append((temp, i))

        return res
        