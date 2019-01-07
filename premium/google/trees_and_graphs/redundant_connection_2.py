'''
https://leetcode.com/explore/interview/card/google/61/trees-and-graphs/366/
'''
class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        can1, can2 = [-1, -1], [-1, -1]
        parent = [0] * (len(edges) + 1)
        
        for i in range(len(edges)):
            if parent[edges[i][1]] != 0:
                can1 = [parent[edges[i][1]], edges[i][1]]
                can2 = [edges[i][0], edges[i][1]]
                edges[i][1] = 0
            parent[edges[i][1]] = edges[i][0]

        for i in range(len(edges)):
            parent[i] = i
        for i in range(len(edges)):
            if edges[i][1] == 0:
                continue
            v, w = edges[i][0], edges[i][1]

            # cycle was detected
            if self.root(parent, v) == w:
                if can1 == [-1, -1]:
                    return edges[i]
                return can1
            parent[w] = v
        
        return can2

    def root(self, parent, i):
        while i != parent[i]:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

sol = Solution()
edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
res = sol.findRedundantDirectedConnection(edges)
print('Expecting [4, 1]: {}'.format(res))

edges2 = [[1,2],[1,3],[2,3]]
res2 = sol.findRedundantDirectedConnection(edges2)
print('Expecting [2,3]: {}'.format(res2))
