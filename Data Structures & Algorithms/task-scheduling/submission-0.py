import heapq
from collections import defaultdict, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = defaultdict(int)
        for task in tasks:
            freqs[task] += 1

        max_heap = []
        for task, count in freqs.items():
            max_heap.append((-count, task))
        heapq.heapify(max_heap)

        q = deque()
        res = 0

        while max_heap or q:
            if q:
                t, count, task = q[0]
                if t <= res:
                    q.popleft()
                    heapq.heappush(max_heap, (count, task))

            if len(max_heap) > 0:
                count, task = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    q.append((res + n + 1, count, task))

            res += 1

        return res
        