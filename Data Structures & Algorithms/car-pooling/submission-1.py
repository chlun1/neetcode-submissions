import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        dropoff_heap = []
        curr_p = 0  # Current number of passengers in car

        for p, s, e in trips:
            while dropoff_heap and dropoff_heap[0][0] <= s:
                prev_e, prev_p = heapq.heappop(dropoff_heap)
                # Drop off passengers
                curr_p -= prev_p

            curr_p += p
            if curr_p > capacity:
                return False

            heapq.heappush(dropoff_heap, (e, p))

        return True
        