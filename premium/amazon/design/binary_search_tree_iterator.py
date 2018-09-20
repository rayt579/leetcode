# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_onto_stack(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0


    def next(self):
        """
        :rtype: int
        """
        node = self.stack.pop()
        if node.right:
            self.push_onto_stack(node.right)
        return node.val

    def push_onto_stack(self, node):
        curr = node
        while curr:
            self.stack.append(curr)
            curr = curr.left


# Your BSTIterator will be called like this:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)
i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print(v)
