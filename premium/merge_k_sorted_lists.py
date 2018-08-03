'''
https://leetcode.com/explore/interview/card/amazon/77/linked-list/512/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for i, listnode in enumerate(lists):
            if listnode:
                heapq.heappush(min_heap, (listnode.val, i))
        merged = ListNode('sentinel')
        merge_ptr = merged
        while len(min_heap) > 0:
            smallest_i = heapq.heappop(min_heap)[1]
            smallest_node = lists[smallest_i]
            merge_ptr.next = smallest_node
            merge_ptr = merge_ptr.next
            lists[smallest_i] = smallest_node.next
            if smallest_node.next != None:
                heapq.heappush(min_heap, (smallest_node.next.val, smallest_i))
        return merged.next


a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

c = ListNode(2)
c.next = ListNode(6)

sol = Solution()
merge = sol.mergeKLists([a,b,c])
curr = merge
while curr:
    print(curr.val)
    curr = curr.next
