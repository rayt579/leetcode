'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        to_visit = deque([(root, 0)])
        level = 0
        values_at_level = []
        overall = []

        while len(to_visit) > 0:
            node, current_level = to_visit.popleft()
            if current_level > level:
                overall.append(values_at_level)
                values_at_level = [node.val]
                level = current_level
            else:
                values_at_level.append(node.val)

            if node.left:
                to_visit.append((node.left, current_level + 1))
            if node.right:
                to_visit.append((node.right, current_level + 1))

        overall.append(values_at_level)
        return overall

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print('Traversal: {}'.format(sol.levelOrder(root)))

