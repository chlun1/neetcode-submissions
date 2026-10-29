import heapq


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = 1000 # We know from the constraints that l, r <= 1000
        r = 0  
        for _, s, e in trips:
            l = min(l, s)
            r = max(r, e)

        passenger_changes = [0] * (r - l + 1)
        for p, s, e in trips:
            passenger_changes[s - l] += p
            passenger_changes[e - l] -= p

        curr_passengers = 0
        for change in passenger_changes:
            curr_passengers += change
            if curr_passengers > capacity:
                return False

        return True
