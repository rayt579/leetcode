'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/504/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.total = None

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sum_numbers_recursive_clean(root)

    def sum_numbers_recursive(self, root):
        self.total = 0
        if not root:
            return 0
        path = [str(root.val)]
        def dfs(root):
            if root.left is None and root.right is None:
                self.total += int(''.join(path))
            else:
                if root.left:
                    path.append(str(root.left.val))
                    dfs(root.left)
                if root.right:
                    path.append(str(root.right.val))
                    dfs(root.right)
            path.pop()
        dfs(root)
        return self.total

    def sum_numbers_recursive_clean(self, root):
        def helper(root, s):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                return s*10 + root.val
            return helper(root.left, s * 10 + root.val) + helper(root.right, s * 10 + root.val)
        return helper(root, 0)


sol = Solution()

tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)

b = TreeNode(4)
b.left = TreeNode(9)
b.right = TreeNode(0)
b.left.left = TreeNode(5)
b.left.right = TreeNode(1)

c = TreeNode(0)
c.left = TreeNode(5)
c.right = TreeNode(9)

print('Expecting 25: {}'.format(sol.sumNumbers(tree)))
print('Expecting 1026: {}'.format(sol.sumNumbers(b)))
print('Expecting 14: {}'.format(sol.sumNumbers(c)))

