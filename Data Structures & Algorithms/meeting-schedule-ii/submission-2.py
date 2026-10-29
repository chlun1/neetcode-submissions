"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        start = sorted(i.start for i in intervals)
        end = sorted(i.end for i in intervals)
        s, e = 0, 0
        count = 0
        res = 0

        while s < n and e < n:
            if start[s] < end[e]:
                count += 1
                res = max(res, count)
                s += 1

            if s < n and start[s] >= end[e]:
                e += 1
                count -= 1

        return res
