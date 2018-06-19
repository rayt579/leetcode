'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lowest_common_ancestor_recursive(root, p, q)

    def lowest_common_ancestor_recursive(self, root, p, q):
        if root.val > p.val and root.val > q.val:
            return self.lowest_common_ancestor_recursive(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowest_common_ancestor_recursive(root.right, p, q)
        return root

sol = Solution()
tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(8)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(9)


print('Expect 6: {}'.format(sol.lowest_common_ancestor_recursive(tree, tree.left, tree.right).val))
print('Expect 2: {}'.format(sol.lowest_common_ancestor_recursive(tree, tree.left, tree.left.right).val))
print('Expect 6: {}'.format(sol.lowest_common_ancestor_recursive(tree, tree.right.left, tree.left.right.left).val))
