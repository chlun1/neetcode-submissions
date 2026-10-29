import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(res, (dist, [x, y]))

        return [x[1] for x in heapq.nsmallest(k, res)]
        