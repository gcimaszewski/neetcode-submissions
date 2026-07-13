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
        
        # Process meetings chronologically by start time.
        # schedule = sorted(intervals, key=lambda i: i.start)
        # heap = []

        # min_meeting_rooms = 0
        # for interval in schedule:
        #     if not heap or interval.start < heap[0]:
        #         heapq.heappush(heap, interval.end)
        #     else:
        #        # while heap and interval.start >= heap[0]:
        #         _ = heapq.heappop(heap)
        #         heapq.heappush(heap, interval.end)
            
        #     # if len(heap) > min_meeting_rooms:
        #     #     min_meeting_rooms =len(heap)
        
        # return len(heap)

        #schedule = sorted(intervals, key=lambda i: i.start)
        start_times = sorted(map(lambda i: i.start, intervals))
        end_times = sorted(map(lambda i: i.end, intervals))
        idx_start = 0
        idx_end = 0
        meetings_active = 0
        max_rooms = 0
        while idx_start < len(intervals):
            # check if the meeting at this slot conflict
            if start_times[idx_start] < end_times[idx_end]:
                meetings_active += 1
                max_rooms = max(max_rooms, meetings_active)
                idx_start += 1
            else:
                meetings_active -=1
                idx_end += 1
        return max_rooms
