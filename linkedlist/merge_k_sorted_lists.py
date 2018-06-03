'''
https://leetcode.com/problems/merge-k-sorted-lists/description/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution:
    # O(n) time complexity, O(1) space
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        min_heap = []
        merge_list = ListNode('sentinel')
        merge_head = merge_list
        for index, head in enumerate(lists):
            if head is not None:
                heapq.heappush(min_heap, (head.val, index))
        while min_heap:
            sorted_list_index = heapq.heappop(min_heap)[1]
            node = lists[sorted_list_index]
            merge_list.next = node
            merge_list = merge_list.next
            next_node = node.next
            lists[sorted_list_index] = next_node

            if next_node is not None:
                heapq.heappush(min_heap, (next_node.val, sorted_list_index))
        return merge_head.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(7)
b = ListNode(3)
b.next = ListNode(5)
c = ListNode(4)
c.next = ListNode(6)
c.next.next = ListNode(8)
sol = Solution()
d = sol.mergeKLists([a])
while d:
    print(d.val)
    d = d.next
