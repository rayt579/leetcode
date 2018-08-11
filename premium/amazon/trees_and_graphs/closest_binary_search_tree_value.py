'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/516/
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.closest_value_recursive(root, target)

    def closest_value_iterative(self, root, target):
        curr = root
        closest = root.val
        while curr:
            if abs(curr.val - target) < abs(closest - target):
                closest = curr.val
            if curr.val > target:
                curr = curr.left
            else:
                curr = curr.right
        return closest

    def closest_value_recursive(self, root, target):
        closest = root.val
        child = root.left if target < root.val else root.right
        if not child:
            return closest
        closest_in_child = self.closest_value_recursive(child, target)
        return min(closest, closest_in_child, key=lambda x: abs(target - x))


sol = Solution()
tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(5)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)

print('Expecting 4: {}'.format(sol.closestValue(tree, 3.71)))
print('Expecting 5: {}'.format(sol.closestValue(tree, 20.8)))
print('Expecting 3: {}'.format(sol.closestValue(tree, 3.4)))

