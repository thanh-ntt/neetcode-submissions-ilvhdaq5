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
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, 0))
        times.sort()
        res = 0
        count = 0
        for t in times:
            if t[1] == 1:
                count += 1
                res = max(count, res)
            else:
                count -= 1
        return res