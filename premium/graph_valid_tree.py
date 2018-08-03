'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/520/
'''

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        nodes = list(range(n))
        for a, b in edges:
            while nodes[a] != a:
                a = nodes[a]
            while nodes[b] != b:
                b = nodes[b]
            if a == b:
                return False
            nodes[a] = b

        return len(edges) == n - 1


sol = Solution()
print('Expecting True: {}'.format(sol.validTree(5, [[0,1],[0,2],[0,3],[1,4]])))
print('Expecting False: {}'.format(sol.validTree(5, [[0, 1],[1,2],[2,3],[1,3],[1,4]])))

