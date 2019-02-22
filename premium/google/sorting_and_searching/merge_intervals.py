# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':
        merged = []
        intervals.sort(key=lambda i: i.start)
        for interval in intervals:
            if len(merged) > 0 and self.has_overlap(interval, merged[-1]):
                merged[-1].end = max(interval.end, merged[-1].end)
            else:
                merged.append(interval)
        return merged

    def has_overlap(self, a, b):
        return a.end >= b.start and b.end >= a.start

sol = Solution()
intervals = [Interval(1,3), Interval(2,6), Interval(8,10), Interval(15, 18)]
merged = sol.merge(intervals)
for i in merged:
    print((i.start, i.end))
