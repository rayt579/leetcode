'''
https://leetcode.com/problems/linked-list-cycle/description/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow, fast = head, head.next
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

sol = Solution()
list_with_cycle = ListNode('A')
b = ListNode('B')
list_with_cycle.next = b
print('Expecting false: {}'.format(sol.hasCycle(list_with_cycle)))
c = ListNode('C')
list_with_cycle.next.next = c
c.next = b
print('Expecting true: {}'.format(sol.hasCycle(list_with_cycle)))


