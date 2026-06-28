import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        occupied_rooms = []
        count = [0] * n
        for start, end in meetings:
            duration = end - start
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _, room = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room)
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room))
            else:
                earliest_end, room = heapq.heappop(occupied_rooms)
                heapq.heappush(
                    occupied_rooms,
                    (earliest_end + duration, room)
                )
            
            count[room] += 1
        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
        