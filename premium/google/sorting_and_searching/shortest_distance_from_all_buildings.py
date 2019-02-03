from collections import deque

class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        m, n = len(grid), len(grid[0])
        min_distance, num_buildings = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        expected_num_buildings = sum([1 for i in range(m) for j in range(n) if grid[i][j] == 1])

        def bfs(start_i, start_j):
            visited = set()
            visited.add((start_i, start_j))
            queue = deque([(start_i, start_j, 0)])
            while len(queue) > 0:
                i, j, dist = queue.popleft()
                for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                        visited.add((x,y))
                        if grid[x][y] == 0:
                            min_distance[x][y] += dist + 1
                            num_buildings[x][y] += 1
                            queue.append((x, y, dist + 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
        
        shortest_distance = float('inf')
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and num_buildings[i][j] == expected_num_buildings:
                    shortest_distance = min(shortest_distance, min_distance[i][j])

        return -1 if shortest_distance == float('inf') else shortest_distance

sol = Solution()
grid = [[1, 0, 2, 0, 1],[0, 0, 0, 0, 0],[0, 0, 1, 0, 0]]
res = sol.shortestDistance(grid)
print('Expecting 7: {}'.format(res))
