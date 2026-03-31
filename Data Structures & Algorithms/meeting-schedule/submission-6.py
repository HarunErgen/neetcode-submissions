"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2: return True

        intervals.sort(key=lambda x: x.start)

        for i in range(1, len(intervals)):
            i2, i1 = intervals[i], intervals[i-1]

            if i2.start < i1.end:
                return False
        return True