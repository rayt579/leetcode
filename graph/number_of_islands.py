from collections import deque
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        return self.num_islands_dfs(grid)
    
    def num_islands_dfs(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0
        m, n = len(grid), len(grid[0])
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.flood_land(grid, i, j, m, n)
                    num_islands += 1

        return num_islands

    def flood_land(self, grid, i, j, m, n):
        grid[i][j] = '0'
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                self.flood_land(grid, x, y, m, n)

    def num_islands_bfs(self, grid):
        if not grid or len(grid[0]) == 0:
            return 0

        m, n = len(grid), len(grid[0])
        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    num_islands += 1
                    self.flood_island(grid, i, j)
        
        return num_islands

    def flood_island(self, grid, i, j):
        queue = deque([(i, j)])
        m, n = len(grid), len(grid[0])

        while queue:
            x, y = queue.popleft()
            if grid[x][y] == '1':
                grid[x][y] = '0'
                for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= next_x < m and 0 <= next_y < n and grid[next_x][next_y] == '1':
                        queue.append((next_x, next_y))
 

