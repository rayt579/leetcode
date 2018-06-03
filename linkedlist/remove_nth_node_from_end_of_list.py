'''
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        sentinel = ListNode('sentinel')
        sentinel.next = head
        curr, fwd = sentinel, sentinel
        for i in range(n):
            fwd = fwd.next
            if fwd is None:
                return head
        while fwd.next is not None:
            fwd = fwd.next
            curr = curr.next

        next_node = curr.next
        curr.next = next_node.next
        next_node.next = None
        return sentinel.next


sol = Solution()
linkedlist = ListNode(1)
linkedlist.next = ListNode(2)
linkedlist.next.next = ListNode(3)
linkedlist.next.next.next = ListNode(4)
linkedlist.next.next.next.next = ListNode(5)

newlist = sol.removeNthFromEnd(linkedlist, 2)
curr = newlist
while curr:
    print(curr.val)
    curr = curr.next
