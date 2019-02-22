# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        i, merged = 0, []
        while i < len(intervals) and intervals[i].end < newInterval.start:
            merged.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval = Interval(min(intervals[i].start, newInterval.start), max(intervals[i].end, newInterval.end))
            i += 1
        merged.append(newInterval)
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1
        return merged

sol = Solution()
intervals = [Interval(4, 10), Interval(12, 20)]
res = sol.insert(intervals, Interval(10, 15))
print((res[0].start, res[0].end))
