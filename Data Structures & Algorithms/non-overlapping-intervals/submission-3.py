class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        res = 0
        prev_end = intervals[0][1]

        for curr in intervals[1:]:
            # Doesn't overlap
            if prev_end <= curr[0]:
                prev_end = curr[1]
            else:
                prev_end = min(prev_end, curr[1])
                res += 1

        return res
