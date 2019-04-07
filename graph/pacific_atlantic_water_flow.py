from collections import deque
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        return self.pacific_atlantic_bfs(matrix)

    def pacific_atlantic_bfs(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return []
        
        m, n = len(matrix), len(matrix[0])
        reaches_pacific = [[False for _ in range(n)] for _ in range(m)]
        reaches_atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            self.bfs(matrix, i, 0, reaches_pacific)
            self.bfs(matrix, i, n - 1, reaches_atlantic)

        for j in range(n):
            self.bfs(matrix, 0, j, reaches_pacific)
            self.bfs(matrix, m - 1, j, reaches_atlantic)

        reaches_both_oceans = []
        for i in range(m):
            for j in range(n):
                if reaches_atlantic[i][j] and reaches_pacific[i][j]:
                    reaches_both_oceans.append((i, j))

        return reaches_both_oceans

    def bfs(self, matrix, i, j, reaches_ocean):
        if reaches_ocean[i][j]:
            return
        queue = deque([(i, j)])
        while queue:
            x, y = queue.popleft()
            if not reaches_ocean[x][y]:
                reaches_ocean[x][y] = True
                for next_x, next_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= next_x < len(matrix) and \
                       0 <= next_y < len(matrix[0]) and \
                       not reaches_ocean[next_x][next_y] and \
                       matrix[next_x][next_y] >= matrix[x][y]:
                           queue.append((next_x, next_y))
    

    def pacific_atlantic_dfs(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or len(matrix[0]) == 0:
            return []

        m, n = len(matrix), len(matrix[0])
        reaches_pacific = [[False for _ in range(n)] for _ in range(m)]
        reaches_atlantic = [[False for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            self.dfs(reaches_pacific, i, 0, matrix, m, n)
            self.dfs(reaches_atlantic, i, n - 1, matrix, m, n)
        
        for i in range(n):
            self.dfs(reaches_pacific, 0, i, matrix, m, n)
            self.dfs(reaches_atlantic, m - 1, i, matrix, m, n)

        reaches_both_oceans = []
        for i in range(m):
            for j in range(n):
                if reaches_pacific[i][j] and reaches_atlantic[i][j]:
                    reaches_both_oceans.append([i, j])
        return reaches_both_oceans

    def dfs(self, visited, i, j, grid, m, n):
        visited[i][j] = True
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] >= grid[i][j] and not visited[x][y]:
                self.dfs(visited, x, y, grid, m, n)
