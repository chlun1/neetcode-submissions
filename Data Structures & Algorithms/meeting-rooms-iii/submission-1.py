import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        if n == 1:
            return 0
            
        meetings.sort(key=lambda x: x[0])
        rooms = list(range(n))
        heapq.heapify(rooms)
        pending = []
        counter = [0] * n

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]

            while pending and pending[0][0] <= start:
                _, room_idx = heapq.heappop(pending)
                heapq.heappush(rooms, room_idx)
                
            if not rooms:
                room_end, room_idx = heapq.heappop(pending)
                end = room_end + (end - start)
            else:
                room_idx = heapq.heappop(rooms)

            counter[room_idx] += 1
            heapq.heappush(pending, (end, room_idx))

        max_count = 0
        max_idx = None
        for i, count in enumerate(counter):
            if count > max_count:
                max_idx = i
                max_count = count

        return max_idx
        