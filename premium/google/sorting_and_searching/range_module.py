class RangeModule:
    def __init__(self):
        self.interval_map = {}

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if left >= right:
            return 

        start, end = self.floorkey(left), self.floorkey(right)

        if not start and not end:
            self.interval_map[left] = right
        elif start and left <= self.interval_map[start]:
            self.interval_map[start] = max(self.interval_map[start], self.interval_map[end], right)
        else:
            self.interval_map[left] = max(self.interval_map[end], right)

        for k in list(self.interval_map):
            if left < k <= right:
                del self.interval_map[k]

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        start = self.floorkey(left)
        if not start:
            return False
        return self.interval_map[start] >= right
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: void
        """
        if left >= right:
            return

        start, end = self.floorkey(left), self.floorkey(right)

        if end and right < self.interval_map[end]:
            self.interval_map[right] = self.interval_map[end]
        if start and left < self.interval_map[start]:
            self.interval_map[start] = left

        for k in list(self.interval_map):
            if left <= k < right:
                del self.interval_map[k]
    
    def floorkey(self, k):
        floor = [i for i in self.interval_map if i <= k]
        if len(floor) == 0:
            return None
        return max(floor)
            

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
print('Expecting True: {}'.format(obj.queryRange(10, 14)))
print('Expecting False: {}'.format(obj.queryRange(13, 15)))
print('Expecting True: {}'.format(obj.queryRange(16, 17)))
