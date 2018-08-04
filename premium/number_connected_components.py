'''
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
'''

import collections
class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        return self.count_components_dfs_iterative(n, edges)

    def count_components_unionfind(self, n, edges):
        roots = list(range(n))
        num_connected = n
        if not edges or len(edges) == 0:
            return num_connected
        for v, w in edges:
            while roots[v] != v:
                roots[v] = roots[roots[v]]
                v = roots[v]
            while roots[w] != w:
                roots[w] = roots[roots[w]]
                w = roots[w]
            if roots[v] != roots[w]:
                roots[v] = roots[w]
                num_connected -= 1
        return num_connected

    def count_components_dfs_recursive(self, n, edges):
        def _dfs(i, graph, is_visited):
            is_visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    _dfs(j, graph, is_visited)

        graph = collections.defaultdict(set)
        for v, w in edges:
            graph[v].add(w)
            graph[w].add(v)
        visited = set()
        connected_count = 0
        for i in range(n):
            if i not in visited:
                _dfs(i, graph, visited)
                connected_count += 1
        return connected_count

    def count_components_dfs_iterative(self, n, edges):
        if not edges or len(edges) == 0:
            return n

        visited = set()
        graph = collections.defaultdict(set)
        for v, w in edges:
            graph[v].add(w)
            graph[w].add(v)

        num_connected = 0
        for i in range(n):
            if i not in visited:
                explore = [i]
                num_connected += 1
                while len(explore) > 0:
                    v = explore.pop()
                    visited.add(v)
                    for w in graph[v]:
                        if w not in visited:
                            explore.append(w)
        return num_connected


sol = Solution()
print('Expecting 2: {}'.format(sol.countComponents(5, [[0,1],[1,2],[3,4]])))
print('Expecting 1: {}'.format(sol.countComponents(5, [[0,1],[1,2],[2,3], [3,4]])))
print('Expecting 1: {}'.format(sol.countComponents(3, [[1,0],[0,2],[2,1]])))
