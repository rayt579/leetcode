'''
https://leetcode.com/problems/number-of-islands/submissions/1
'''


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        island_count = 0
        if not grid:
        	return island_count
        directions = [[0,-1], [0,1],[-1,0],[1,0]]
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    explore = [(i, j)]
                    while len(explore) > 0:
                        curr_i, curr_j = explore.pop()
                        grid[curr_i][curr_j] = '0'
                        for x, y in directions:
                            next_i, next_j = curr_i + x, curr_j + y
                            if 0 <= next_i < m and 0 <= next_j < n and grid[next_i][next_j] == '1':
                                explore.append((next_i, next_j))
                    island_count += 1
        return island_count

sol = Solution()
grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','0']]
print('Expect 3: {}'.format(sol.numIslands(grid)))
