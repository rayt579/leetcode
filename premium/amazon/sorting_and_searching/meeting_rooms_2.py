# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __lt__(self, other):
        return self.end < other.end

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        return self.min_meeting_rooms_array(intervals)

    def min_meeting_rooms_array(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()
        rooms, endItr = 0, 0

        for i in range(len(starts)):
            if starts[i] < ends[endItr]:
                rooms += 1
            else:
                endItr += 1
        return rooms

    def min_meeting_rooms_heapq(self, intervals):
        if not intervals or len(intervals) == 0:
            return 0
        rooms = []
        intervals.sort(key= lambda i: i.start)
        heapq.heappush(rooms, (intervals[0].end, intervals[0]))
        for i in range(1, len(intervals)):
            interval = heapq.heappop(rooms)[1]
            if intervals[i].start >= interval.end:
                interval.end = intervals[i].end
            else:
                heapq.heappush(rooms, (intervals[i].end, intervals[i]))
            heapq.heappush(rooms, (interval.end, interval))
        return len(rooms)

a = [Interval(0, 30), Interval(5,10), Interval(15,20)]
b = [Interval(7,10), Interval(2,4)]
c = [Interval(5, 8), Interval(6,8)]

sol = Solution()
#print('Expect 2: {}'.format(sol.minMeetingRooms(a)))
#print('Expect 1: {}'.format(sol.minMeetingRooms(b)))
print('Expect : {}'.format(sol.minMeetingRooms(c)))
