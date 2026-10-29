import heapq


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        m = len(queries)
        intervals.sort(key=lambda x: x[0])
        q_indices = list(range(m))
        q_indices.sort(key=lambda i: queries[i])
        available = []
        res = [-1] * m
        i = 0

        for q in q_indices:
            query = queries[q]
            while i < n and intervals[i][0] <= query:
                l, r = intervals[i]
                heapq.heappush(available, (r - l + 1, r))
                i += 1

            while available and available[0][1] < query:
                heapq.heappop(available)

            if available:
                res[q] = available[0][0]

        return res
