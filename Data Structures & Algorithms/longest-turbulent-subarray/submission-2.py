class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res, curr = 1, 1
        sign = 0

        for i in range(1, len(arr)):
            if arr[i - 1] < arr[i]:
                if sign != -1:
                    curr += 1
                    sign = -1
                else:
                    curr = 2
                    sign = -1
            elif arr[i - 1] > arr[i]:
                if sign != 1:
                    curr += 1
                    sign = 1
                else:
                    curr = 2
                    sign = 1
            else:
                curr = 1
                sign = 0

            res = max(res, curr)

        return res
                