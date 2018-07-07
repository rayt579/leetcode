'''
https://leetcode.com/problems/add-two-numbers/description/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode('sentinel')
        result = head
        carry = 0
        while l1 != None or l2 != None:
            top_value = l1.val if l1 != None else 0
            bottom_value = l2.val if l2 != None else 0
            result.next = ListNode((top_value + bottom_value + carry) % 10)
            carry = 0 if top_value + bottom_value + carry < 10 else 1

            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

            result = result.next

        if carry == 1:
            result.next = ListNode(1)

        return head.next

sol = Solution()
a = ListNode(9)
a.next = ListNode(9)
a.next.next = ListNode(9)
b = ListNode(9)
b.next = ListNode(9)
b.next.next = ListNode(9)

res = sol.addTwoNumbers(a, b)
while res:
    print(res.val)
    res = res.next
