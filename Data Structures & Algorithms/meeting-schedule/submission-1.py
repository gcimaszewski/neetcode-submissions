"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        schedule = sorted(intervals, key=lambda i: (i.start, i.end))
        for idx in range(1, len(schedule)):
            start = schedule[idx].start
            prev_end = schedule[idx-1].end
            if start < prev_end:
                return False
        
        return True