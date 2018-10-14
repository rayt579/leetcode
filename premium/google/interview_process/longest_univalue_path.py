'''
https://leetcode.com/explore/interview/card/google/67/sql-2/473/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue = deque([root])
        longest_path = float('-inf')
        visited = set()

        while len(queue) > 0:
            node = queue.popleft()
            if node not in visited:
                longest_path = max(longest_path, self.longest_path_at_node(node, 0, visited))

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return longest_path

    def longest_path_at_node(self, node, count, nodes_visited):
        if not node:
            return count

        nodes_visited.add(node)
        if node.left and node.left.val == node.val:
            count += self.longest_path_at_node(node.left, count + 1, nodes_visited)
        if node.right and node.right.val == node.val:
            count += self.longest_path_at_node(node.right, count + 1, nodes_visited)
        return count

sol = Solution()
tree = TreeNode(5)
tree.left = TreeNode(4)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(1)
tree.right = TreeNode(5)
tree.right.right = TreeNode(5)

print('Expecting 2: {}'.format(sol.longestUnivaluePath(tree)))
