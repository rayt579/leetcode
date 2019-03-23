# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr and curr.next:
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = curr
            if prev:
                prev.next = next_node
            else:
                head = next_node
            prev, curr = curr, curr.next
        return head

sol = Solution()
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
res = sol.swapPairs(head)

def print_llist(node):
    curr = node
    while curr:
        print(curr.val)
        curr = curr.next
print_llist(res)
