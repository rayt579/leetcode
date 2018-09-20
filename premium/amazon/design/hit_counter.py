'''
https://leetcode.com/explore/interview/card/amazon/81/design/518/
'''
from collections import defaultdict, deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.times = [0] * 300
        self.hits = [0] * 300


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        index = timestamp % 300
        if self.times[index] != timestamp:
            self.times[index] = timestamp
            self.hits[index] = 1
        else:
            self.hits[index] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        hit_count = 0
        for i in range(300):
            if timestamp - self.times[i] < 300:
                hit_count += self.hits[i]
        return hit_count

class HitCounterQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = deque()


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.timestamps.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        while len(self.timestamps) > 0 and timestamp - self.timestamps[0] >= 300:
            self.timestamps.popleft()
        return len(self.timestamps)

class HitCounterInefficient:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counts = defaultdict(int)


    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.counts[timestamp] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        hit_count = 0
        for i in range(timestamp - 299, timestamp + 1):
            if i >= 0 and i in self.counts:
                hit_count += self.counts[i]
        return hit_count



# Your HitCounter object will be instantiated and called as such:
hc = HitCounter()
hc.hit(1)
hc.hit(2)
hc.hit(3)
print('Expect 3: {}'.format(hc.getHits(4)))
hc.hit(300)
print('Expect 4: {}'.format(hc.getHits(300)))
print('Expect 3: {}'.format(hc.getHits(301)))
