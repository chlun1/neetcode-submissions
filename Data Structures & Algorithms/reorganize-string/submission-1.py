import heapq
from collections import Counter, deque


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        max_heap = [(-cnt, c) for c, cnt in char_counts.items()]
        heapq.heapify(max_heap)

        res = []
        q = deque()
        while max_heap or q:
            if q and q[0][0] <= len(res):
                _, cnt, c = q.popleft()
                heapq.heappush(max_heap, (cnt, c))

            if not max_heap:
                break

            cnt, c = heapq.heappop(max_heap)
            res.append(c)
            cnt += 1
            if cnt < 0:
                q.append((len(res) + 1, cnt, c))

        return "".join(res) if len(res) == len(s) else ""
        