'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/519/
'''
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
        curr, ancestor = root, None
        while curr:
            if curr.val < p.val:
                curr = curr.right
            elif curr.val > p.val:
                ancestor = curr
                curr = curr.left
            else:
                if curr.right:
                    curr = curr.right
                    while curr.left:
                        curr = curr.left
                    return curr
                return ancestor

        return None


sol = Solution()
tree = TreeNode(5)
tree.left = TreeNode(3)
tree.right = TreeNode(6)
tree.left.left = TreeNode(2)
tree.left.right = TreeNode(4)
tree.left.left.left = TreeNode(1)

print('Expect 5: {}'.format(sol.inorderSuccessor(tree, tree.left.right).val))


