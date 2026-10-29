class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        res = []
        added = False
        prev = [-1, -1]
        i = 0

        while i < len(intervals):
            if not added and (prev[0] <= newInterval[0] <= intervals[i][0]):
                curr = newInterval
                added = True
            else:
                curr = intervals[i]
                i += 1

            if prev[1] >= curr[0]:
                res[-1][1] = max(prev[1], curr[1])
            else:
                res.append(curr)

            prev = res[-1]

        if not added:
            if res[-1][1] >= newInterval[0]:
                res[-1][1] = max(res[-1][1], newInterval[1])
            else:
                res.append(newInterval)

        return res
