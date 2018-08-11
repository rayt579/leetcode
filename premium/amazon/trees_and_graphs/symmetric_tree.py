'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/507/
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.is_symmetric_iterative(root)

    def is_symmetric_recursive(self, root):
        if root is None:
            return True
        return self.symmetric_tree_helper(root.left, root.right)

    def symmetric_tree_helper(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.symmetric_tree_helper(left.left, right.right) and self.symmetric_tree_helper(left.right, right.left)

    def is_symmetric_iterative(self, root):
        if root is None:
            return True
        explore = [(root.left, root.right)]
        while len(explore) > 0:
            left, right = explore.pop()
            if (not left and right) or (not right and left):
                return False
            if left and right:
                if left.val != right.val:
                    return False
                explore.append((left.right, right.left))
                explore.append((left.left, right.right))

        return True




sol = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(3)
a.left.right = TreeNode(4)
a.right = TreeNode(2)
a.right.left = TreeNode(4)
a.right.right = TreeNode(3)

b = TreeNode(1)
b.left = TreeNode(2)
b.left.right = TreeNode(3)
b.right = TreeNode(2)
b.right.right = TreeNode(3)

print('Expecting True: {}'.format(sol.isSymmetric(a)))
print('Expecting False: {}'.format(sol.isSymmetric(b)))
