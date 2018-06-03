'''
https://leetcode.com/problems/lru-cache/description/

Takeaways:
1) OrderedDict can function as a LRU cache if you do not want to implement your own Double-Linked List, HashMap
2) Remember to evict only when a new element is added to the cache.
'''

from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
        	value = self.cache.pop(key)
        	self.cache[key] = value
        	return value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
        	self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
        	self.cache.popitem(last=False)
        self.cache[key] = value

cache = LRUCache(2)
cache.put(1,1)
cache.put(2, 2)
print('Expecting 1: {}'.format(cache.get(1)))
cache.put(3, 3)
print('Expecting -1: {}'.format(cache.get(2)))
