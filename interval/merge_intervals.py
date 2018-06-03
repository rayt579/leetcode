'''
https://leetcode.com/problems/merge-intervals/description/
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        intervals.sort(key=lambda interval:interval.start)
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            if self.has_overlap(merged_intervals[-1], intervals[i]):
                merged_intervals[-1].start = min(merged_intervals[-1].start, intervals[i].start)
                merged_intervals[-1].end = max(merged_intervals[-1].end, intervals[i].end)
            else:
                merged_intervals.append(intervals[i])

        return merged_intervals

    def has_overlap(self, a, b):
        return a.start <= b.end and a.end >= b.start

sol = Solution()
intervals = sol.merge([Interval(1,3), Interval(2,6), Interval(8,10), Interval(15, 18)])
for interval in intervals:
    print('Start: {}, End: {}'.format(interval.start, interval.end))

print(sol.merge([]))
print(sol.merge([[],[]]))


