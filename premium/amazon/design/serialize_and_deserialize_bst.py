# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "null"
        message = []
        def build_message(root):
            if root is None:
                message.append('null')
            else:
                message.append(str(root.val))
                build_message(root.left)
                build_message(root.right)
        build_message(root)
        return ','.join(message)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        queue = collections.deque(data.split(','))
        def build_tree():
            val = queue.popleft()
            if val == 'null':
                return None
            root = TreeNode(val)
            root.left = build_tree()
            root.right = build_tree()
            return root
        return build_tree()

def print_tree(root):
    if root is None:
        return
    print(root.val)
    print_tree(root.left)
    print_tree(root.right)


# Your Codec object will be instantiated and called as such:
codec = Codec()
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
message = codec.serialize(tree)
print('Serialize: {}'.format(message))
print('Deserialize')
print_tree(codec.deserialize(message))
# codec.deserialize(codec.serialize(root))
