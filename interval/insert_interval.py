'''
https://leetcode.com/problems/insert-interval/description/
'''

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]

        merged_intervals = []
        insert_added = False

        for interval in intervals:
            if interval:
                if self.is_overlap(interval, newInterval):
                    if not insert_added:
                        merged_intervals.append(self.merge_intervals(interval, newInterval))
                        insert_added = True
                    else:
                        merged_intervals[-1] = self.merge_intervals(interval, newInterval)
                    newInterval = merged_intervals[-1]
                elif newInterval.end < interval.start and not insert_added:
                    merged_intervals.append(newInterval)
                    merged_intervals.append(interval)
                    insert_added = True
                else:
                    merged_intervals.append(interval)

        if not insert_added:
            merged_intervals.append(newInterval)

        return merged_intervals

    def is_overlap(self, a, b):
        return a.start <= b.end and a.end >= b.start

    def merge_intervals(self, a, b):
        return Interval(min(a.start, b.start), max(a.end, b.end))


sol = Solution()
a = [Interval(1,3), Interval(6, 9)]
merged = sol.insert(a, Interval(2, 5))
print('Intervals to merge: [1, 3], [6, 9]     Insert: [2, 5]')
for interval in merged:
    print('[{}, {}]'.format(interval.start, interval.end))


b = [Interval(1,2), Interval(3,5), Interval(6,7), Interval(8,10), Interval(12,16)]
merged_b = sol.insert(b, Interval(4,9))
print('Intervals to merge: [1, 2], [3, 5], [6, 7], [8, 10], [12, 16]     Insert: [4, 9]')
for interval in merged_b:
    print('[{}, {}]'.format(interval.start, interval.end))

