'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/487/
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.find_target_inorder_array(root, k)

    def find_target_inorder_array(self, root, k):
        nums = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
        if root is None:
            return False
        inorder(root)
        i, j = 0, len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == k:
                return True
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return False

    def find_target_recursive_set(self, root, k):
        values = set()
        def dfs(root, k):
            if root is None:
                return False
            if k - root.val in values:
                return True
            values.add(root.val)
            return dfs(root.left, k) or dfs(root.right, k)
        return dfs(root, k)

    def find_target_using_binarysearch(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        explore = deque([root])
        while len(explore) > 0:
            node = explore.popleft()
            target = k - node.val
            if target != node.val and self.binary_search(root, target):
                return True
            if node.left:
                explore.append(node.left)
            if node.right:
                explore.append(node.right)
        return False

    def binary_search(self, root, target):
        if root is None:
            return False
        if root.val < target:
            return self.binary_search(root.right, target)
        elif root.val > target:
            return self.binary_search(root.left, target)
        else:
            return True

a = TreeNode(5)
a.left = TreeNode(3)
a.left.left = TreeNode(2)
a.left.right = TreeNode(4)
a.right = TreeNode(6)
a.right.right = TreeNode(7)

sol = Solution()
print('Expecting true: {}'.format(sol.findTarget(a, 9)))
print('Expecting false: {}'.format(sol.findTarget(a, 28)))
print('Expecting false: {}'.format(sol.findTarget(TreeNode(1), 2)))

