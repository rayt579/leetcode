'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/488/
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.is_subtree_recursive(s, t)

    def is_subtree_recursive(self, s, t):
        def is_same_tree(a, b):
            if a is None or b is None:
                return a == b
            if a.val != b.val:
                return False
            return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)

        if s is None:
            return False
        if s.val == t.val and is_same_tree(s, t):
            return True
        return self.is_subtree_recursive(s.left, t) or self.is_subtree_recursive(s.right, t)

sol = Solution()
s = TreeNode(3)
s.left = TreeNode(4)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.right = TreeNode(5)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)

u = TreeNode(4)
u.left = TreeNode(1)
u.right = TreeNode(2)

print('Expecting True: {}'.format(sol.isSubtree(s, t)))
t.right.left = TreeNode(0)
print('Expecting False: {}'.format(sol.isSubtree(s, t)))
print('Expecting True: {}'.format(sol.isSubtree(s, u)))
