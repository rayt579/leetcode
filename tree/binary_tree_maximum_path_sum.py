class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    max_path_sum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_path_sum = float('-inf')
        self.max_path_down(root)
        return self.max_path_sum

    def max_path_down(self, node):
        if not node:
            return 0
        left = self.max_path_down(node.left)
        right = self.max_path_down(node.right)
        self.max_path_sum = max(self.max_path_sum, node.val, node.val + left, node.val + right, node.val + left + right)

        return max(max(left, right) + node.val, node.val)


sol = Solution()

tree_one = TreeNode(1)
tree_one.left = TreeNode(2)
tree_one.right = TreeNode(3)
print('Expecting 6: {}'.format(sol.maxPathSum(tree_one)))


tree_two = TreeNode(-10)
tree_two.left = TreeNode(9)
tree_two.right = TreeNode(20)
tree_two.right.left = TreeNode(15)
tree_two.right.right = TreeNode(7)
print('Expecting 42: {}'.format(sol.maxPathSum(tree_two)))


tree_three = TreeNode(5)
tree_three.left = TreeNode(4)
tree_three.right = TreeNode(8)
tree_three.left.left = TreeNode(11)
tree_three.right.left = TreeNode(13)
tree_three.right.right = TreeNode(4)
tree_three.left.left.left = TreeNode(7)
tree_three.left.left.right = TreeNode(2)
tree_three.right.right.right = TreeNode(1)
print('Expect 48: {}'.format(sol.maxPathSum(tree_three)))
