import heapq
from collections import deque


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q_heap = []
        p_heap = []

        for idx in range(len(tasks)):
            et, pt = tasks[idx][0], tasks[idx][1]
            heapq.heappush(q_heap, (et, pt, idx))

        t = 0
        res = []

        while q_heap or p_heap:
            while q_heap and q_heap[0][0] <= t:
                et, pt, idx = heapq.heappop(q_heap)
                heapq.heappush(p_heap, (pt, idx))

            if p_heap:
                pt, idx = heapq.heappop(p_heap)
                res.append(idx)
                t += pt
            else:
                t = q_heap[0][0]

        return res
        