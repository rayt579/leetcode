'''
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
'''

import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        encoded_string = []
        def build_string(node):
            if not node:
                encoded_string.append('None')
            else:
                encoded_string.append(str(node.val))
                build_string(node.left)
                build_string(node.right)
        build_string(root)
        return ','.join(encoded_string)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data or len(data) == 0:
            return None

        explore = collections.deque(data.split(','))

        def create_tree():
            node_val = explore.popleft()
            if node_val == 'None':
                return None
            node = TreeNode(node_val)
            node.left = create_tree()
            node.right = create_tree()
            return node

        return create_tree()

def preorder(root):
    if not root:
        return
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# VLR
def preorder_iterative(root):
    if not root:
        return
    explore = [root]
    while len(explore) > 0:
        node = explore.pop()
        print(node.val)
        if node.right:
            explore.append(node.right)
        if node.left:
            explore.append(node.left)
# LVR
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def inorder_iterative(root):
    if not root:
        return
    curr = root
    explore = []
    while curr:
        explore.append(curr)
        curr = curr.left
    while len(explore) > 0:
        node = explore.pop()
        print(node.val)
        if node.right:
            curr = node.right
            while curr:
                explore.append(curr)
                curr = curr.left

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val)

# Your Codec object will be instantiated and called as such:
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.right.left = TreeNode(4)
tree.right.right = TreeNode(5)

codec = Codec()
ser = codec.serialize(tree)
print('Serialize into: {}'.format(ser))

deser = codec.deserialize(ser)
print('Deserialize into tree: ')
preorder(deser)


print('Preorder:')
preorder(deser)

print('Preorder Iterative:')
preorder_iterative(deser)

print('Inorder:')
inorder(deser)

print('Inorder Iterative:')
inorder_iterative(deser)

print('Postorder')
postorder(deser)
