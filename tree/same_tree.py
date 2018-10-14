'''
https://leetcode.com/problems/same-tree/description/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        path_p = self.get_bfs_path(p)
        path_q = self.get_bfs_path(q)

        if len(path_p) != len(path_q):
            return False

        for i in range(len(path_p)):
            if not path_p[i] or not path_q[i]:
                if path_p[i] != path_q[i]:
                    return False
            elif path_p[i].val != path_q[i].val:
                return False

        return True

    def get_bfs_path(self, root):
        if root is None:
            return [None]

        path = []
        to_visit = deque([root])

        while to_visit:
            curr_node = to_visit.popleft()
            path.append(curr_node)
            if curr_node and (curr_node.left or curr_node.right):
                to_visit.append(curr_node.left)
                to_visit.append(curr_node.right)

        #self.print_path(path)
        return path

    def print_path(self, path):
        to_print = []
        for node in path:
            if node is None:
                to_print.append(None)
            else:
                to_print.append(node.val)

        print('**DEBUG** Tree path: {}'.format(to_print))

sol = Solution()
a = TreeNode(1)
a.left = TreeNode(2)
a.left.right = TreeNode(4)
a.right = TreeNode(3)

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
b.left.left = TreeNode(4)

print(sol.isSameTree(a, b))



a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(3)
print(sol.isSameTree(a, b))
