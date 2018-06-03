'''
https://leetcode.com/problems/reverse-linked-list/description/
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reverse_list_recursive(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        rest =  self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return rest


print('ABC')
a = ListNode('A')
a.next = ListNode('B')
a.next.next = ListNode('C')
sol = Solution()
reversed_a = sol.reverseList(a)

while reversed_a:
    print(reversed_a.val)
    reversed_a = reversed_a.next
