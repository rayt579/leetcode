'''
https://leetcode.com/explore/interview/card/google/60/linked-list-5/1342/
'''
# Definition for a Node.
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head, insertVal):
        """
        :type head: Node
        :type insertVal: int
        :rtype: Node
        """
        new_node = Node(insertVal, None)
        if not head:
            new_node.next = new_node
            return new_node
        a, b = head, head.next

        while True:
            if a.val <= insertVal <= b.val:
                break
            elif a.val > b.val and (insertVal < b.val or insertVal > a.val):
                break
            a, b = a.next, b.next 
            if a == head:
                break
        
        a.next = new_node
        new_node.next = b
        return head

sol = Solution()
head = Node(3, None)
head.next = Node(4, None)
head.next.next = Node(1, None)
head.next.next.next = head

res = sol.insert(head, 5)
curr = head
while True:
    print(curr.val)
    curr = curr.next
    if curr == head:
        break
