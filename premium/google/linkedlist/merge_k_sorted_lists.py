# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        merge = ListNode('sentinel')
        ptr = merge
        for i, llist in enumerate(lists):
            if llist:
                heapq.heappush(min_heap,(llist.val, i, llist))
        while len(min_heap) > 0:
            _, curr_i, curr_node = heapq.heappop(min_heap)
            ptr.next = curr_node
            if curr_node.next:
                heapq.heappush(min_heap, (curr_node.next.val, curr_i, curr_node.next))
            ptr = ptr.next
        return merge.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)

llist = [b, c, a]
sol = Solution()
res = sol.mergeKLists(llist)
curr = res
while curr:
    print(curr.val)
    curr = curr.next
