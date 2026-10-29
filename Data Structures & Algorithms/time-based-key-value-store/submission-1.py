from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.m = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.m[key]
        if not arr:
            return ""

        if timestamp < arr[0][1]:
            return ""

        l, r = 0, len(arr) - 1
        res = ""

        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return res
