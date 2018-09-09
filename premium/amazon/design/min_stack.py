'''
https://leetcode.com/explore/interview/card/amazon/81/design/503/
'''
class MinWithCount:
    def __init__(self, val):
        self.val = val
        self.count = 1

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.cache = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.cache) == 0:
            self.cache.append(MinWithCount(x))
            self.stack.append(x)
            return

        self.stack.append(x)
        if x == self.cache[-1].val:
            self.cache[-1].count += 1
        elif x < self.cache[-1].val:
            self.cache.append(MinWithCount(x))

    def pop(self):
        """
        :rtype: void
        """
        if len(self.stack) == 0:
            raise Exception('Cannot pop from an empty stack!')
        val = self.stack.pop()
        if val == self.cache[-1].val:
            self.cache[-1].count -= 1
            if self.cache[-1].count == 0:
                self.cache.pop()
        return val

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            raise Exception('Cannot top from an empty stack')
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.cache[-1].val


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print('Expect -3: {}'.format(minStack.getMin()))
minStack.pop()
print('Expect 0: {}'.format(minStack.top()))
print('Expect -2: {}'.format(minStack.getMin()))
