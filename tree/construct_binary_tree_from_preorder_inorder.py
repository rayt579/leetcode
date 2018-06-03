'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        preorder = deque(preorder)
        def construct_tree(in_start, in_end):
            node = TreeNode(preorder.popleft())
            if in_start == in_end:
                return node
            node_index = inorder.index(node.val)
            if node_index > in_start:
                node.left = construct_tree(in_start, node_index - 1)
            if node_index < in_end:
                node.right = construct_tree(node_index + 1, in_end)
            return node

        return construct_tree(0, len(inorder) - 1)

preorder_path = []
def preorder(node):
    if node == None:
        return
    preorder_path.append(node.val)
    preorder(node.left)
    preorder(node.right)

inorder_path = []
def inorder(node):
    if node == None:
        return
    inorder(node.left)
    inorder_path.append(node.val)
    inorder(node.right)

sol = Solution()
preorder_list = [7, 10, 4, 3, 1, 2, 8, 11]
inorder_list = [4, 10, 3, 1, 7, 11, 8, 2]
tree = sol.buildTree(preorder_list, inorder_list)

preorder(tree)
inorder(tree)
print('Preorder path: {}'.format(preorder_path))
print('Inorder path: {}'.format(inorder_path))
