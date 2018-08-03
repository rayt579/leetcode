# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque, defaultdict
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        visit = deque([(root, 0)])
        columns = defaultdict(list)
        while len(visit) > 0:
            node, col_index = visit.popleft()
            columns[col_index].append(node.val)
            if node.left:
                visit.append((node.left, col_index - 1))
            if node.right:
                visit.append((node.right, col_index + 1))
        return [columns[i] for i in sorted(columns.keys())]

sol = Solution()
tree = TreeNode(3)
tree.left = TreeNode(9)
tree.right = TreeNode(15)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(20)

print('Expecting [[9], [3, 7], [15], [20]]: {}'.format(sol.verticalOrder(tree)))
