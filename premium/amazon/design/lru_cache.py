'''
https://leetcode.com/explore/interview/card/amazon/81/design/478/
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.size = 0
        self.head = None
        self.last = None
        self.capacity = capacity
        self.data = {}


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.data:
            return -1
        node = self.data[key]
        self.__remove(node)
        self.__insert_node_as_head(node)
        return node.val


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.data:
            node = self.data[key]
            node.val = value
            self.__remove(node)
            self.__insert_node_as_head(node)
        else:
            if self.size == self.capacity:
                self.data.pop(self.last.key)
                self.__remove(self.last)
            node = Node(key, value)
            self.__insert_node_as_head(node)
            self.data[key] = node

    def __insert_node_as_head(self, node):
        if node is None:
            raise Exception("Need Node object!")
        if self.head is None and self.last is None:
            self.head, self.last = node, node
        else:
            node.prev, node.next = None, self.head
            self.head = node
            node.next.prev = self.head

        self.size += 1

    def __remove(self, node):
        if not node:
            raise Exception("Need Node object!")

        prev_node, next_node = node.prev, node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

        if node == self.head and node == self.last:
            self.head, self.last = None, None
        elif node == self.head:
            self.head = next_node
        elif node == self.last:
            self.last = prev_node

        node.prev = None
        node.next = None
        self.size -= 1

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.get(1)
print('Expecting head at 1: {} last at 2: {}'.format(cache.head.val, cache.last.val))
cache.put(3,3)
print('Expecting head at 3: {} last at 1: {}'.format(cache.head.val, cache.last.val))
res = cache.get(2)
print('Expecting -1: {}'.format(res))
cache.put(4,4)
print('Expecting head at 4: {} last at 3: {}'.format(cache.head.val, cache.last.val))
res = cache.get(1)
print('Expecting -1: {}'.format(res))
res = cache.get(3)
print('Expecting 3: {}'.format(res))
res = cache.get(4)
print('Expecting 4: {}'.format(res))
