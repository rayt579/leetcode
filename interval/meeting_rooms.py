'''
https://leetcode.com/problems/meeting-rooms/description/
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        if not intervals:
            return True
        intervals.sort(key= lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i-1].end:
                return False
        return True

a = [Interval(0, 30), Interval(5,10), Interval(15,20)]
b = [Interval(7, 10), Interval(2,4)]
c = [Interval(7,10), Interval(7,10)]
sol = Solution()

print('Expecting False: {}'.format(sol.canAttendMeetings(a)))
print('Expecting True: {}'.format(sol.canAttendMeetings(b)))
print('Expecting False: {}'.format(sol.canAttendMeetings(c)))

