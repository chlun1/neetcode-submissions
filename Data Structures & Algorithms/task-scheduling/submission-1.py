import heapq
from collections import defaultdict, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = defaultdict(int)
        for task in tasks:
            freqs[task] += 1

        max_heap = []
        for task, count in freqs.items():
            max_heap.append(-count)
        heapq.heapify(max_heap)

        q = deque()
        res = 0

        while max_heap or q:
            if q and q[0][0] <= res:
                _, count = q.popleft()
                heapq.heappush(max_heap, count)

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    q.append((res + n + 1, count))

            res += 1

        return res
        