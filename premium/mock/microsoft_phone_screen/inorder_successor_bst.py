# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        return self.inorder_successor_recursive(root, p)

    def inorder_successor_recursive(self, root, p):
        if not root:
            return None
        if p.val < root.val:
            left = self.inorder_successor_recursive(root.left, p)
            return left if left else root
        else:
            return self.inorder_successor_recursive(root.right, p)

    def inorder_successor_iterative(self, root, p):
        parent, curr = None, root
        while curr:
            if p == curr:
                if curr.right:
                    successor = curr.right
                    while successor.left:
                        successor = successor.left
                    return successor
                else:
                    return parent
            elif p.val < curr.val:
                parent = curr
                curr = curr.left
            else:
                curr = curr.right

        return None
        
root = TreeNode(5)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(6)

p = root.right
q = root.left.right
sol = Solution()
print('Expecting None: {}'.format(sol.inorderSuccessor(root, p)))
print('Expecting 5: {}'.format(sol.inorderSuccessor(root, q).val))
