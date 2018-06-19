'''
https://leetcode.com/problems/validate-binary-search-tree/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque, namedtuple
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        NodeWithMinMax = namedtuple('NodeWithMinMax', ['node', 'min_val', 'max_val'])
        tree = NodeWithMinMax(root, float('-inf'), float('inf'))
        explore = deque([tree])

        while len(explore) > 0:
            current = explore.popleft()
            if current.node.val <= current.min_val or current.node.val >= current.max_val:
                return False
            if current.node.left:
                explore.append(NodeWithMinMax(current.node.left, current.min_val, current.node.val))
            if current.node.right:
                explore.append(NodeWithMinMax(current.node.right, current.node.val, current.max_val))

        return True

    def is_valid_bst_recursive(self, root):
        def helper(root, min_val, max_val):
            if root is None:
                return True
            if root.val <= min_val or root.val >= max_val:
                return False
            return helper(root.left, min_val, root.val) and helper(root.right, root.val, max_val)

        return helper(root, float('-inf'), float('inf'))

    def is_valid_bst_recursive_inefficient(self, root):
        if root is None:
            return True
        return self.tree_less_than(root.left, root.val) and self.tree_greater_than(root.right, root.val) and self.is_valid_bst_recursive(root.left) and self.is_valid_bst_recursive(root.right)

    def tree_less_than(self, root, value):
        if root is None:
            return True
        if root.val >= value:
            return False
        return self.tree_less_than(root.left, value) and self.tree_less_than(root.right, value)

    def tree_greater_than(self, root, value):
        if root is None:
            return True
        if root.val <= value:
            return False
        return self.tree_greater_than(root.left, value) and self.tree_greater_than(root.right, value)


sol = Solution()

tree1 = TreeNode(2)
tree1.left = TreeNode(1)
tree1.right = TreeNode(3)

tree2 = TreeNode(5)
tree2.left = TreeNode(1)
tree2.right = TreeNode(4)
tree2.right.left = TreeNode(3)
tree2.right.right = TreeNode(6)

print('Expect true: {}'.format(sol.isValidBST(tree1)))
print('Expect false: {}'.format(sol.isValidBST(tree2)))
