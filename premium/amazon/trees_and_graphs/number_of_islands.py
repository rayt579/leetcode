'''
https://leetcode.com/explore/interview/card/amazon/78/trees-and-graphs/894/
'''


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or len(grid[0]) == 0:
            return 0
        num_islands = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        def dfs(grid, i, j):
            if grid[i][j] == '1':
                grid[i][j] = '0'
                for a, b in directions:
                    next_i, next_j = i + a, j + b
                    if 0 <= next_i < m  and 0 <= next_j < n:
                        dfs(grid, next_i, next_j)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    dfs(grid, i, j)
        return num_islands

sol = Solution()
grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]
print('Expecting 3: {}'.format(sol.numIslands(grid)))
