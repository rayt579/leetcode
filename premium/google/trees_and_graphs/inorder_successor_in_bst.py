# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        ancestor, curr = None, root
        while True:
            if p.val > curr.val:
                curr = curr.right
            elif p.val < curr.val:
                ancestor, curr = curr, curr.left
            else:
                if curr.right:
                    successor = curr.right
                    while successor.left: 
                        successor = successor.left
                    return successor
                else:
                    return ancestor
    
    def inorderSuccessorRecursive(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if p.val < root.val:
            left = self.inorderSuccessorRecursive(root.left, p)
            return root if not left else left
        return self.inorderSuccessorRecursive(root.right, p)

    def inorderPredecessorRecursive(self, root, p):
        if not root:
            return None
        if p.val <= root.val:
            return self.inorderPredecessorRecursive(root.left, p)
        right = self.inorderPredecessorRecursive(root.right, p)
        return root if not right else right

bst = TreeNode(10)
bst.left = TreeNode(5)
bst.left.left = TreeNode(1)
bst.left.right = TreeNode(8)
bst.right = TreeNode(15)
bst.right.left = TreeNode(12)
bst.right.right = TreeNode(17)

sol = Solution()
print('Expect 12: {}'.format(sol.inorderSuccessorRecursive(bst, bst).val))
print('Expect 12: {}'.format(sol.inorderPredecessorRecursive(bst, bst.right).val))
