"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        cloned_nodes = {}
        def clone_nodes(node):
            if not node:
                return None
            if node.val in cloned_nodes:
                return cloned_nodes[node.val]
            
            clone = Node(node.val, [])
            cloned_nodes[node.val] = clone

            for neighbor in node.neighbors:
                if neighbor.val not in cloned_nodes:
                    clone.neighbors.append(cloned_nodes(neighbor))
                else:
                    clone.neighbors.append(cloned_nodes[neighbor.val])
            return clone

        return clone_nodes(node)
