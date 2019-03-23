# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        return self.lca_iterative(root, p, q)

    def lca_iterative(self, root, p, q):
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
        return None 

    def lca_recursive(self, root, p, q):
        def helper(root):
            if root.val < p.val and root.val < q.val:
                return helper(root.right)
            elif root.val > p.val and root.val > q.val:
                return helper(root.left)
            else:
                return root
        return helper(root)

    def lca_submission(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = deque([root])
        candidates = []
        while len(queue) > 0:
            node = queue.popleft()
            if self.exists_in_bst(node, p.val) and self.exists_in_bst(node, q.val):
                candidates.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return candidates[-1]

    def exists_in_bst(self, bst, val):
        curr = bst
        while curr:
            if curr.val == val:
                return True
            if curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        return False

sol = Solution()
tree = TreeNode(6)
tree.left = TreeNode(2)
tree.left.left = TreeNode(0)
tree.left.right = TreeNode(4)
tree.left.right.left = TreeNode(3)
tree.left.right.right = TreeNode(5)
tree.right = TreeNode(8)
tree.right.left = TreeNode(7)
tree.right.right = TreeNode(9)
p, q = tree.left, tree.left.right
res = sol.lowestCommonAncestor(tree, p, q)
print('Expecting 2: {}'.format(res.val))
