'''
https://leetcode.com/problems/reorder-list/submissions/1
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or head.next is None:
            return

        # find middle of linkedlist
        mid, fast = head, head
        while fast.next and fast.next.next:
            mid = mid.next
            fast = fast.next.next

        # reverse after mid
        prev, curr = mid.next, mid.next.next
        prev.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        mid.next = prev

        # merge lists
        left = head
        right = mid.next
        while left != mid:
            next_left = left.next
            next_right = right.next
            left.next = right
            right.next = next_left
            left = next_left
            right = next_right
        left.next = right

sol = Solution()
nom = ListNode(1)
nom.next = ListNode(2)
nom.next.next= ListNode(3)
nom.next.next.next = ListNode(4)
sol.reorderList(nom)
while nom:
    print(nom.val)
    nom = nom.next
