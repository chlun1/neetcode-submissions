import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = [x for x in ((-a, "a"), (-b, "b"), (-c, "c")) if x[0] < 0]
        heapq.heapify(max_heap)

        res = []
        prev = None

        while max_heap or prev:
            if not max_heap:
                break
            
            cnt, c = heapq.heappop(max_heap)
            res.append(c)
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None

            if cnt < 0:
                if len(res) > 1 and res[-2] == res[-1] == c:
                    prev = (cnt, c)
                else:
                    heapq.heappush(max_heap, (cnt, c))

        return "".join(res)
