'''
https://leetcode.com/explore/interview/card/google/67/sql-2/473/
'''
# Definition for a binary tree root.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.max_path_length = 0

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longest_path_at(node, val):
            if not node: return 0
            left = 0 if not node.left else longest_path_at(node.left, node.val)
            right = 0 if not node.right else longest_path_at(node.right, node.val)
            
            self.max_path_length = max(self.max_path_length, left + right)
            if node.val == val: 
                return max(left, right) + 1
            return 0
        
        longest_path_at(root, None)
        return self.max_path_length
        



        

sol = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

tree = TreeNode(1)
tree.left = TreeNode(4)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(4)
tree.right = TreeNode(5)
tree.right.right = TreeNode(5)

complete = TreeNode(4)
complete.left = TreeNode(4)
complete.left.left = TreeNode(4)
complete.left.right = TreeNode(4)
complete.right = TreeNode(4)
complete.right.left = TreeNode(4)
complete.right.right = TreeNode(4)


print('Expecting 2: {}'.format(sol.longestUnivaluePath(root)))
print('Expecting 2: {}'.format(sol.longestUnivaluePath(tree)))
print('Expecting 4: {}'.format(sol.longestUnivaluePath(complete)))
