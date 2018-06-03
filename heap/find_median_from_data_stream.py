'''
https://leetcode.com/problems/find-median-from-data-stream/submissions/1
'''
import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.left, -num)
        heapq.heappush(self.right, -heapq.heappop(self.left))
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        return float(-self.left[0])


mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print('Expecting median of 1.5: {}'.format(mf.findMedian()))
mf.addNum(3)
print('Expecting median of 2: {}'.format(mf.findMedian()))
