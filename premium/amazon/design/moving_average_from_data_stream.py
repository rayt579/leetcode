from collections import deque
class MovingAverage:
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.data = []
        self.size = size
        self.front = 0
        self.total = 0


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.total += val
        if len(self.data) == self.size:
            self.total -= self.data[self.front]
            self.data[self.front] = val
            self.front = (self.front + 1) % self.size
        else:
            self.data.append(val)
        return self.total / len(self.data)

class MovingAverageQueue:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = deque()
        self.size = size


    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.popleft()
        return sum(self.queue) / len(self.queue)



# Your MovingAverage object will be instantiated and called as such:
m = MovingAverage(3)
print('Expect 1: {}'.format(m.next(1)))
print('Expect 5.5: {}'.format(m.next(10)))
print('Expect 4.6: {}'.format(m.next(3)))
print('Expect 6: {}'.format(m.next(5)))
