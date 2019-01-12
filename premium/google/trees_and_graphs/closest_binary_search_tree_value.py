 #Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest, min_difference = None, float('inf')
        curr = root
        while curr:
            difference = abs(curr.val - target)
            if difference < min_difference:
                closest, min_difference = curr.val, difference
            if target < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return closest

root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(8)
root.left.right = TreeNode(15)
root.right = TreeNode(30) 
root.right.left = TreeNode(25)
root.right.right = TreeNode(40)

sol = Solution()
print('Expecting 8: {}'.format(sol.closestValue(root, -100.0)))
print('Expecting 15: {}'.format(sol.closestValue(root, 17.4)))
print('Expecting 40: {}'.format(sol.closestValue(root, 1000.00)))
