'''
https://leetcode.com/explore/interview/card/amazon/79/sorting-and-searching/497/
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
    def __eq__(self, other):
        print('Start: Compare {} to {}'.format(self.start, other.start))
        print('End: Compare {} to {}'.format(self.end, other.end))

        return self.start == other.start and self.end == other.end

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        return self.min_meeting_rooms_bf(intervals)

    def min_meeting_rooms_bf(self, intervals):
        if not intervals:
            return 0

        min_rooms = 1
        for i in range(1, len(intervals)):
            overlap_count = 0
            for j in range(i):
                print(i, j)
                if self.has_overlap(intervals[i], intervals[j]):
                    overlap_count += 1
                elif intervals[i] == intervals[j]:
                    overlap_count += 2
            if overlap_count == i:
                min_rooms += 1
        return min_rooms

    def has_overlap(self, a, b):
        return a.start < b.end and b.start < a.end

    def comp(self, i1, i2):
        return i1.start == i2.start and i1.end == i2.end

sol = Solution()
a = [Interval(15, 20), Interval(5, 10), Interval(0, 30)]
b = [Interval(7, 10), Interval(2,4)]
c = [Interval(1, 5), Interval(8, 9), Interval(8,9)]
#print('Expecting 2: {}'.format(sol.minMeetingRooms(a)))
#print('Expecting 1: {}'.format(sol.minMeetingRooms(b)))
print('Expecting 2: {}'.format(sol.minMeetingRooms(c)))
