'''
https://leetcode.com/explore/interview/card/amazon/81/design/495/
'''
import heapq
class MedianFinder:

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
        if len(self.left) + len(self.right) == 0:
            raise Exception('No median for an empty stream')
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (-self.left[0] + self.right[0])/2.0
        else:
            return float(-self.left[0])



# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(1)
print('Expecting 1: {}'.format(obj.findMedian()))
obj.addNum(2)
print('Expecting 1.5: {}'.format(obj.findMedian()))
obj.addNum(3)
print('Expecting 2: {}'.format(obj.findMedian()))
obj.addNum(4)
print('Expecting 2.5: {}'.format(obj.findMedian()))


