'''
https://leetcode.com/problems/invert-binary-tree/description/
'''

# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

from collections import deque
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        visit = deque([root])
        while len(visit) > 0:
            node = visit.popleft()
            if node.left or node.right:
                node.left, node.right = node.right, node.left
            if node.left:
                visit.append(node.left)
            if node.right:
                visit.append(node.right)
        return root

    def invert_tree_recursive(self, root):
        if root is None:
            return None
        if root.left or root.right:
            root.left, root.right = root.right, root.left
        root.left = self.invert_tree_recursive(root.left)
        root.right = self.invert_tree_recursive(root.right)
        return root

tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.right = TreeNode(9)
tree.right.left = TreeNode(6)

def print_tree(root):
    queue = deque([root])
    while len(queue) > 0:
        node = queue.popleft()
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

print_tree(tree)
sol = Solution()
sol.invertTree(tree)
#sol.invert_tree_recursive(tree)
print('Inverted tree: ')
print_tree(tree)
