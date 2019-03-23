class Solution:
    def minPathSum(self, grid):
        return self.min_path_sum_dp_linear_space(grid)

    def min_path_sum_dp_linear_space(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])

        prev, curr = [float('inf') for _ in range(n + 1)], [float('inf') for _ in range(n + 1)]
        curr[n] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                curr[j] = min(curr[j + 1], prev[j]) + grid[i][j]
                #print('({}, {}): {}'.format(i, j, curr[j]))
            prev = curr
            curr = [float('inf') for _ in range(n + 1)]
        return prev[0]

    def min_path_sum_dp_straightforward(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        
        # Base case
        dp[m][n - 1] = 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]
                #print('mps at ({},{}): {}'.format(i, j, dp[i][j]))

        return dp[0][0]

    def min_path_top_down_recursive(self, grid):
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])
        results = {}

        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            point = (i, j)
            if point in results:
                return results[point]
            min_path_sum = float('inf')
            for x, y in [(i, j + 1), (i + 1, j)]:
                if 0 <= x < m and 0 <= y < n:
                    min_path_sum = min(min_path_sum, dfs(x, y))
            min_path_sum += grid[i][j]
            results[point] = min_path_sum
            return min_path_sum

        return dfs(0, 0)
sol = Solution()
res = sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]])
print('Expecting 7: {}'.format(res))
