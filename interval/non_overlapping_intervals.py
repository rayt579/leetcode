'''
https://leetcode.com/problems/non-overlapping-intervals/description/
'''

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals or len(intervals) == 1:
            return 0

        intervals.sort(key=lambda i:i.start)
        a,b = 0, 1
        count_remove = 0
        while a < len(intervals) and b < len(intervals):
            if self.intervals_overlap(intervals[a],intervals[b]):
                a = min(a, b, key=lambda i: intervals[i].end)
                count_remove += 1
            else:
                a = b
            b += 1
        return count_remove

    def intervals_overlap(self, a, b):
        return b.start < a.end and b.end > a.start


sol = Solution()
a = [Interval(1,2), Interval(2,3), Interval(3,4), Interval(1,3)]
b = [Interval(1,2), Interval(1,2), Interval(1,2)]
c = [Interval(1,2), Interval(2,3)]

print('Expect 1: {}'.format(sol.eraseOverlapIntervals(a)))
print('Expect 2: {}'.format(sol.eraseOverlapIntervals(b)))
print('Expect 0: {}'.format(sol.eraseOverlapIntervals(c)))



