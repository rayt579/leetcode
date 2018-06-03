'''
https://leetcode.com/problems/clone-graph/description/
'''

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

import collections

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        return self._clone_graph(node, {})

    def _clone_graph(self, original_node, cloned_nodes):
        if original_node is None:
            return None

        if original_node in cloned_nodes:
            return cloned_nodes[original_node]

        clone_node = UndirectedGraphNode(original_node.label)
        cloned_nodes[original_node] = clone_node

        for neighbor in original_node.neighbors:
            if neighbor not in cloned_nodes:
                clone_node.neighbors.append(self._clone_graph(neighbor, cloned_nodes))
            else:
                clone_node.neighbors.append(cloned_nodes[neighbor])

        return clone_node

    def clone_graph_iterative(self, node):
        if node is None:
            return None

        clones = {}
        clones[node] = UndirectedGraphNode(node.label)
        nodes_to_visit = collections.deque([node])

        while nodes_to_visit:
            original = nodes_to_visit.popleft()

            for neighbor in original.neighbors:
                if neighbor not in clones:
                    clones[neighbor] = UndirectedGraphNode(neighbor.label)
                    nodes_to_visit.append(neighbor)
                clones[original].neighbors.append(clones[neighbor])

        return clones[node]


def print_node_information(node):
    print('***********HEAD*************')
    print('Node: {} with label: {}'.format(node, node.label))
    print('************NEIGHBORS************')
    for neighbor in node.neighbors:
        print('Node: {} with label: {}'.format(neighbor, neighbor.label))

a = UndirectedGraphNode('0')
b = UndirectedGraphNode('1')
c = UndirectedGraphNode('2')
a.neighbors = [b, c]
b.neighbors = [c]
c.neighbors = [c]
print_node_information(a)

print('**************RECURSIVE SOLUTION**********************')
sol = Solution()
clone = sol.cloneGraph(a)
print_node_information(clone)

print('**************ITERATIVE SOLUTION**********************')
sol = Solution()
clone = sol.clone_graph_iterative(a)
print_node_information(clone)