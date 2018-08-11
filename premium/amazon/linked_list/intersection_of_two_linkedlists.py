'''
https://leetcode.com/explore/interview/card/amazon/77/linked-list/515
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        return self.get_intersection_clever(headA, headB)

    def get_intersection(self, headA, headB):
        a, b = headA, headB
        if not a or not b:
            return None

        a_length, b_length = self.helper_get_length(headA), self.helper_get_length(headB)
        while a_length > b_length:
            a = a.next
            a_length -= 1
        while b_length > a_length:
            b = b.next
            b_length -= 1

        while a != b and a != None and b != None:
            a = a.next
            b = b.next

        return a if a == b else None

    def helper_get_length(self, llist):
        if not llist:
            return 0
        length = 0
        while llist != None:
            llist = llist.next
            length += 1
        return length

    def get_intersection_clever(self, A, B):
        if not A or not B:
            return None
        a, b = A, B
        while a != b:
            a = B if not a else a.next
            b = A if not b else b.next
        return a

a = ListNode(7)
b = ListNode(5)
c = ListNode(4)
c.next = ListNode(2)
c.next.next = ListNode(1)
a.next = c
b.next = c

sol = Solution()
intersect = sol.getIntersectionNode(a, b)
print(intersect.val)

