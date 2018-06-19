'''
https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root, k):
        stack = []
        while root != None:
            stack.append(root)
            root = root.left

        while len(stack) > 0:
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            right = node.right

            while right != None:
                stack.append(right)
                right = right.left

        return -1

    def kth_smallest_recursive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def count_nodes(root):
            if root is None:
                return 0
            return 1 + count_nodes(root.left) + count_nodes(root.right)

        if root is None:
            return None

        node_count_left = count_nodes(root.left)
        if node_count_left >= k:
            return self.kth_smallest_recursive(root.left, k)
        elif k > node_count_left + 1:
            return self.kth_smallest_recursive(root.right, k - node_count_left - 1)
        return root.val

    def kth_smallest_preorder(self, root, k):
        preorder = []
        def helper(root):
            if root is None:
                return
            helper(root.left)
            preorder.append(root.val)
            helper(root.right)
        helper(root)
        return preorder[k-1]

sol = Solution()
a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(6)
a.left.left = TreeNode(2)
a.left.right = TreeNode(4)
a.left.left.left = TreeNode(1)


print('Expecting 3: {}'.format(sol.kthSmallest(a, 3)))
