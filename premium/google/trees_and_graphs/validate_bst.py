from collections import deque

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = deque([(root, float('-inf'), float('inf'))])
        
        while len(queue) > 0:
            node, lower_limit, upper_limit = queue.popleft()
            if not lower_limit < node.val < upper_limit:
                return False
            if node.left:
                queue.append((node.left, lower_limit, node.val))
            if node.right:
                queue.append((node.right, node.val, upper_limit))

        return True
