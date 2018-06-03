'''
https://leetcode.com/problems/subtree-of-another-tree/description/
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def is_same_tree(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            if s.val != t.val:
                return False
            return is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)

        explore = [s]
        while len(explore) > 0:
            node = explore.pop()
            if is_same_tree(node, t):
                return True
            else:
                if node.right:
                    explore.append(node.right)
                if node.left:
                    explore.append(node.left)
        return False

sol = Solution()
s_tree = TreeNode(3)
s_tree.left = TreeNode(4)
s_tree.left.left = TreeNode(1)
s_tree.left.right = TreeNode(2)
s_tree.right = TreeNode(5)

t_tree = TreeNode(4)
t_tree.left = TreeNode(1)
t_tree.right = TreeNode(2)

print('Expecting true: {}'.format(sol.isSubtree(s_tree, t_tree)))
s_tree.left.right.left = TreeNode(0)
print('Expecting false: {}'.format(sol.isSubtree(s_tree, t_tree)))
