import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        char_counts = Counter(s)
        max_heap = [(-cnt, c) for c, cnt in char_counts.items()]
        heapq.heapify(max_heap)

        res = []
        prev = None
        while max_heap or prev:
            if prev and not max_heap:
                return ""

            cnt, c = heapq.heappop(max_heap)
            res.append(c)
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt < 0:
                prev = (cnt, c)

        return "".join(res)
        