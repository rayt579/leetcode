'''
https://leetcode.com/problems/binary-tree-level-order-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque, defaultdict
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        nodes_at_level = defaultdict(list)
        explore = deque([(root, 0)])
        while len(explore) > 0:
            node, level = explore.popleft()
            nodes_at_level[level].append(node)
            if node.left:
                explore.append((node.left, level + 1))
            if node.right:
                explore.append((node.right, level + 1))
        return [[node.val for node in nodes_at_level[level]] for level in sorted(nodes_at_level.keys())]

sol = Solution()
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print('Traversal: {}'.format(sol.levelOrder(tree)))
