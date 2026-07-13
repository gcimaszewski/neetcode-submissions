"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        # sort according to finish time
        schedule = sorted(intervals, key=lambda i: i.start)
        heap = []

        min_meeting_rooms = 0
        for interval in schedule:
            if not heap or interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
               # while heap and interval.start >= heap[0]:
                _ = heapq.heappop(heap)
                heapq.heappush(heap, interval.end)
            
            if len(heap) > min_meeting_rooms:
                min_meeting_rooms =len(heap)
        
        return len(heap)
