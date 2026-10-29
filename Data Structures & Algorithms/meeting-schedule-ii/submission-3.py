"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        ends = []
        res = 0

        for interval in intervals:
            if ends and ends[0] <= interval.start:
                heapq.heappop(ends)
            else:
                res += 1

            heapq.heappush(ends, interval.end)

        return res
        