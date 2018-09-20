'''
https://leetcode.com/explore/interview/card/amazon/82/others/897/
'''
class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        if m < 0 or n < 0:
            return []

        num_islands = []
        island_count = 0
        roots = [-1] * m * n
        sizes = [0] * m * n

        for i, j in positions:
            root = n * i + j
            roots[root] = root
            island_count += 1
            sizes[root] += 1
            for x, y in [(0, 1), (0, -1), (-1,0), (1,0)]:
                next_i, next_j = i + x, j + y
                pos = n * next_i + next_j
                if 0 <= next_i < m and 0 <= next_j < n and roots[pos] != -1:
                    neighbor_root = self.find_root(roots, roots[pos])
                    if root != neighbor_root:
                        if sizes[root] < sizes[neighbor_root]:
                            roots[root] = neighbor_root
                            sizes[neighbor_root] += sizes[root]
                            root = neighbor_root
                        else:
                            roots[neighbor_root] = root
                            sizes[root] += sizes[neighbor_root]
                        island_count -= 1
            num_islands.append(island_count)

        return num_islands

    def find_root(self, roots, pos):
        while roots[pos] != pos:
            roots[pos] = roots[roots[pos]]
            pos = roots[pos]
        return pos

sol = Solution()
print('Expect [1,1,2,3]: {}'.format(sol.numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]])))
print('Expect [1,2,1]: {}'.format(sol.numIslands2(3,1,[[0,0],[2,0],[1,0]])))
print('Expect [1, 2, 3, 4, 3, 2, 1]: {}'.format(sol.numIslands2(3,3,[[0,1],[1,2],[2,1], [1,0],[0,2],[0,0],[1,1]])))
