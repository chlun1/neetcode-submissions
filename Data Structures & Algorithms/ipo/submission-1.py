import heapq


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        c_heap = []  # capital
        p_heap = []  # profit
        for i, c in enumerate(capital):
            heapq.heappush(c_heap, (c, i))

        for _ in range(k):
            while c_heap and c_heap[0][0] <= w:
                _, i = heapq.heappop(c_heap)
                heapq.heappush(p_heap, -profits[i])

            if not p_heap:
                break

            w -= heapq.heappop(p_heap)

        return w
        