'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/486/
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct_maximum_binary_tree_recursive(nums)

    def construct_maximum_binary_tree_recursive(self, nums):
        def build_tree_recursive(lo, hi):
            if lo > hi:
                return None
            i = self.find_max_index(nums, lo, hi)
            root = TreeNode(nums[i])
            root.left = build_tree_recursive(lo, i - 1)
            root.right = build_tree_recursive(i + 1, hi)
            return root

        return build_tree_recursive(0, len(nums) - 1)

    def find_max_index(self, arr, lo, hi):
        max_val, max_i = float('-inf'), -1
        while lo <= hi:
            if arr[lo] > max_val:
                max_val = arr[lo]
                max_i = lo
            lo += 1
        return max_i

from collections import deque
def print_bfs(tree):
    print('Performing BFS on tree')
    explore = deque([tree])
    while len(explore) > 0:
        node = explore.popleft()
        print(node.val)
        if node.left:
            explore.append(node.left)
        if node.right:
            explore.append(node.right)

sol = Solution()
tree = sol.constructMaximumBinaryTree([3,2,1,6,0,5])
tree2 = sol.constructMaximumBinaryTree([7,8,9])
tree3 = sol.constructMaximumBinaryTree([35, 40, 21, 50, 24, 42, 30])

print_bfs(tree)
print_bfs(tree2)
print_bfs(tree3)
