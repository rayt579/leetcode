'''
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sentinel = ListNode('sentinel')
        curr = sentinel
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l2 if not l1 else l1

        return sentinel.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(4)

b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)

sol = Solution()
head = sol.mergeTwoLists(a, b)
while head:
    print(head.val)
    head = head.next

