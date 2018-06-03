'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if root is None:
            return 0
        max_depth = 0
        nodes_to_visit = [(root, 1)]

        while nodes_to_visit:
            node, depth = nodes_to_visit.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                nodes_to_visit.append((node.left, depth + 1))
            if node.right:
                nodes_to_visit.append((node.right, depth + 1))

        return max_depth

    def max_depth_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.max_depth_recursive_memoize(root, {})

    def max_depth_recursive_memoize(self, root, max_depths_at_node):
        if root is None:
            return 0
        if root in max_depths_at_node:
            return max_depths_at_node[root]

        max_depth =  max(self.max_depth_recursive_memoize(root.left, max_depths_at_node), self.max_depth_recursive_memoize(root.right, max_depths_at_node)) + 1
        max_depths_at_node[root] = max_depth
        return max_depth


tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
sol = Solution()
print(sol.maxDepth(tree))
